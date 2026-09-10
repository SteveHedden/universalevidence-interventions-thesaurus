# Universal Evidence Interventions Thesaurus

A controlled vocabulary of deliberate actions, services, programs, and policies used to describe interventions across health and development research. Developed by Steve Hedden as part of [Universal Evidence](https://universalevidence.com).

## Contents

Version **0.4.0**. Counts below describe the 8 September 2026 snapshot.

- `interventions.ttl`: 2,784 Interventions, organized by the kind of action or delivery mechanism.

Interventions describe what is done. The conditions they seek to change and metrics used to evaluate them belong to the companion Conditions and Outcomes thesaurus.

## Use

Concepts have stable identifiers under `https://universalevidence.com/vocab/interventions/`. Labels, definitions, and relationships use SKOS. External `exactMatch`, `closeMatch`, and `relatedMatch` links express different strengths of alignment; a related topic is not an equivalent concept.

The vocabulary uses [Universal Evidence Ontology 0.5.0](https://github.com/SteveHedden/universalevidence-ontology). Its exact validation schema is included in `validation/ue-0.5.0.ttl`, under CC BY 4.0. Versions of the thesaurus and ontology are independent.

```python
from rdflib import Graph

g = Graph()
g.parse("interventions.ttl", format="turtle")
print(len(g))
```

## Validation

With Python 3.11 or later:

```sh
python -m pip install -r requirements-validation.txt
python validate.py
```

The validator checks ontology conformance, reference closure, hierarchy cycles, and reciprocal related links. Structural validation does not certify every scientific definition or external alignment. The vocabulary is intended for indexing and evidence discovery.

Registry-specific crosswalks and legacy identifier forwarding are maintained separately by Universal Evidence. They are excluded from this vocabulary distribution. Retired records are removed after reference migration; existing identifiers are preserved through application compatibility mappings where required.

## Attribution and license

[CC BY 4.0](LICENSE) applies to Universal Evidence's vocabulary contributions. Upstream source rights and attribution remain applicable; see [SOURCES.md](SOURCES.md) and `source-manifest.json` for source-text provenance and alignment distinctions.

**Courtesy of the U.S. National Library of Medicine.** NLM does not endorse this vocabulary. This edited snapshot does not necessarily reflect the most current or accurate NLM data. Source citations within definitions have been retained where present.
