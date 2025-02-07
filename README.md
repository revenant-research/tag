# Revenant Research Project

This repository contains code from an ongoing research project by Revenant Research (Revenant AI LLC). This is not intended to be used as a standalone application, but rather serves as a component of our broader research initiatives.

## ⚠️ Important Notice
This is a Work in Progress: The code in this repository is part of an active research project and is not designed to function as a standalone application. It is being shared with the research community in the spirit of open science and collaborative development.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Research Context
TAG is an evolution of Retrieval-Augmented Generation (RAG) aimed at enabling multi-step, goal-oriented workflows in AI applications. Instead of focusing on single-turn Q&A, TAG treats each task as a first-class entity, embedding it in the same vector space as the organization’s knowledge chunks. This allows for persistent, iterative retrieval of only the most relevant information at each phase of a project.

**Core Concept**
Tasks Table: Stores tasks (with names, descriptions, domain labels, and a vector embedding).
Knowledge Chunks Table: Houses segmented text (chunks) from corporate docs, each with a domain label and a vector embedding.
The system retrieves chunks by comparing a task’s embedding to those of the knowledge chunks, yielding semantically relevant matches.
**Advantages**
- Persistent Task Context: Instead of ephemeral prompts, tasks remain in the database, enabling consistent reference across multiple steps.
- Multi-Domain Organization: Both tables track domain_name to filter and group data, ensuring domain-appropriate retrieval.
- Iterative Refinement: Task embeddings can be updated as the project evolves, automatically adjusting which chunks get retrieved.
**Comparison to RAG**
Traditional RAG focuses on single-pass retrieval for Q&A. TAG extends this by offering a multi-step, audit-friendly workflow where tasks drive retrieval at each stage.
**Implementation Note**
Uses pgvector for approximate nearest neighbor search, allowing rapid semantic lookups. Any RAG system can be converted to a TAG system by adding a tasks table and knowledge chunks table.
Recommended embedding dimension typically matches your chosen LLM’s embedding output (e.g., 768).
For a deeper dive—covering architecture, tooling, and real-world use cases—refer to the full TAG white paper by Revenant Research.

## Repository Structure
\`\`\`
project/
├── src/
│   ├── [core components]
├── tests/
│   ├── [test files]
├── docs/
│   ├── [documentation]
└── research/
    └── [research papers and data]
\`\`\`

## Contributing
We welcome contributions from the research community. However, please note:
- This is an active research project, so major architectural changes should be discussed first
- Open an issue before submitting significant pull requests
- Follow our coding standards and documentation requirements
- Include appropriate tests with any code submissions

## Development Setup
1. Clone the repository
2. Install dependencies
3. [Additional setup steps]

## Current Status
- 🔬 Active Research Phase
- 📊 Experimental Features
- 🚧 Under Development

## Citation
\`\`\`bibtex
@misc{revenant2025research,
    title={[Task Augmented Generation]},
    author={Revenant Research},
    year={2025},
    publisher={GitHub},
    howpublished={\url{[repository URL]}}
}
\`\`\`

## Contact
- Research Lead: [Nathan Staffel]
- Email: [nathan@revenantai.com]
- Project Website: [www.revenantresearch.com]


---

**Note**: This repository is maintained by Revenant Research as part of our commitment to open science and collaborative research. While we aim to be responsive to issues and pull requests, our primary focus is on advancing the core research objectives.
