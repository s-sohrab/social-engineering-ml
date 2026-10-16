---
language:
- fa
license: other
task_categories:
- question-answering
- text-generation
tags:
- social-engineering
- cybersecurity
- question-answering
- grounded-generation
- artificial-intelligence
- fa
size_categories:
- 1K<n<10K
---

# Social Engineering Q&A Dataset (Persian / Farsi)

## Overview

A Persian (Farsi) question–answer corpus for social engineering and cybersecurity, derived from curated knowledge articles extracted from authoritative reference books.

This release is part of a bilingual research dataset engineering pipeline designed for
supervised fine-tuning (SFT), retrieval-augmented generation (RAG) evaluation, and
domain-specific language model benchmarking in cybersecurity education.

Each record is grounded in a structured knowledge article and contains:

- `question`: a natural-language question
- `answer`: a concise, article-grounded answer
- `language`: `fa`
- `question_index`: ordinal question identifier within the same article (1–3)
- `source_id`: stable article identifier
- `source`: internal reference-book identifier
- `article_type`: article taxonomy label
- `title_slug`: article slug

## Provenance and Source Corpus

All Q&A pairs were generated from structured JSONL knowledge articles located in the
project directory `Books_Split/`. The upstream articles were extracted from the following
reference books (PDF sources):

- `deep-insight-into-social-engineering.pdf`
- `ESET-Social_engineering_handbook.pdf`
- `Learn-Social-Engineering-Learn-the-Art-of-Human-Hacking-Dr.-Erdal-Ozkaya.pdf`
- `Social-Engineering-Crowdmasters-Gehl-Lawson.pdf`
- `Social-Engineering-in-Cybersecurity-Threats-and-Defenses-Gururaj.pdf`
- `Social-Engineering-The-Science-of-Human-Hacking-Hadnagy.pdf`
- `Social-Engineering-The-Art-of-Human-Hacking-Hadnagy.pdf`
- `Sefreta-Zero-to-Hundred-Social-Engineering.pdf`

The merged knowledge base contains **1,165** article records spanning **8** reference books
on social engineering, human hacking, phishing, pretexting, and organizational security awareness.

## Dataset Statistics

| Metric | Value |
| --- | ---: |
| Total Q&A records | 3,330 |
| Unique knowledge article IDs | 0 |
| Unique reference books | 1 |
| Mean question length (characters) | 81.08 |
| Mean answer length (characters) | 163.48 |
| Question length range (characters) | 12 – 181 |
| Answer length range (characters) | 3 – 481 |

### Question Index Distribution

| question_index | Count |
| --- | ---: |
| 1 | 3,330 |
| 2 | 0 |
| 3 | 0 |

### Records per Reference Book

| Reference Book | Q&A Records |
| --- | ---: |
| unknown | 3330 |

## Generation Methodology

- Articles were first normalized into structured JSONL records (`content_clean`, `summary`,
  `keywords`, `article_type`, etc.).
- Question–answer pairs were generated with **DeepSeek-V4-Pro** under strict grounding constraints:
  answers must be supported only by the source article text.
- Each article contains up to **three distinct questions** (`question_index` 1–3), each available
  in both English and Persian in the bilingual release family.
- Global deduplication was applied at the question-fingerprint level before publication.

## Intended Use

- Instruction tuning for cybersecurity QA assistants
- Evaluation of grounded generation and hallucination resistance
- Cross-lingual alignment studies (English ↔ Persian)
- Educational and research applications in AI security awareness

## Ownership, Legal Notice, and Attribution

**Dataset curator and legal owner of this compiled release:**

- **Samed Sehrab**
- **PhD Student in Artificial Intelligence**

This Hugging Face release represents a curated, value-added compilation of question–answer pairs.
The underlying reference books remain the intellectual property of their respective authors and
publishers. This dataset distributes only derived QA annotations and metadata produced through a
research pipeline; it does not redistribute full book text.

**Academic acknowledgment:**

This work was conducted under the guidance of **Dr. Amir Nazami Saffa**, who served as research
advisor and collaborator throughout dataset design, quality control, and publication preparation.

## Citation

If you use this dataset in academic or industrial research, please cite the dataset repository:

```bibtex
@dataset{sehrab2026socialengineeringqafa,
  title        = {Social Engineering Q&A Dataset (Persian / Farsi)},
  author       = {Sehrab, Samed},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/smd20/social-engineering-qa-persian}},
  note         = {PhD research dataset in Artificial Intelligence. Advisor: Dr. Amir Nazami Saffa.}
}
```

## License

The compiled QA annotations in this repository are released for **research and educational use**.
Users must respect the copyright of the original reference books and comply with applicable
publisher terms. Commercial redistribution of this dataset requires explicit permission from
the dataset owner.

## Repository

- Hugging Face dataset: `smd20/social-engineering-qa-persian`
- Primary data file: `data/train.jsonl`
- Machine-readable statistics: `stats/dataset_statistics.json`

