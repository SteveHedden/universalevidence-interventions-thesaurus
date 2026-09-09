"""Validate this vocabulary release against the bundled ontology and graph rules."""
from pathlib import Path
from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import RDF, SKOS, OWL, SH
from pyshacl import validate

ROOT = Path(__file__).resolve().parent
U = Namespace('https://universalevidence.com/ontology/')
graph = Graph()
for path in ROOT.glob('*.ttl'):
    graph.parse(path)
ontology = Graph().parse(ROOT / 'validation' / 'ue-0.5.0.ttl')
conforms, report, text = validate(graph, shacl_graph=ontology, meta_shacl=True, allow_warnings=False)
assert conforms, text
assert not list(report.subjects(RDF.type, SH.ValidationResult)), text
assert not list(graph.subjects(OWL.deprecated, None))
edges = {}
for s, p, o in graph:
    if p in (U.measures, U.measuredBy, U.bearer, SKOS.broader, SKOS.narrower, SKOS.related):
        assert (o, RDF.type, None) in graph, ('Undefined target', s, p, o)
    if p == SKOS.broader:
        edges.setdefault(s, set()).add(o)
    if p == SKOS.narrower:
        edges.setdefault(o, set()).add(s)
    if p == SKOS.related:
        assert (o, SKOS.related, s) in graph, ('Missing inverse', s, o)
visited, active = set(), set()
def visit(node):
    assert node not in active, ('Hierarchy cycle', node)
    if node in visited:
        return
    active.add(node)
    for parent in edges.get(node, ()):
        visit(parent)
    active.remove(node)
    visited.add(node)
for node in edges:
    visit(node)
print(f'PASS: {len(graph):,} triples; ontology conformance, reference closure, hierarchy, and reciprocal related links.')
