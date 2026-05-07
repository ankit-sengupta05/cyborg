---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:43:03.767917'
id: e5603572
links: []
modified: '2026-05-07T20:43:03.767917'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: COCOMO Models Explained with Example Scenario A University M (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 7fba437ee7be
source: cocomo  all.pdf
page: 0
title: COCOMO Models Explained with Example Scenario A University M (Chunk 0)
keywords: ['COCOMO Models', 'UMS', 'KLOC', 'Intermediate COCOMO', 'Detailed COCOMO', 'COCOMO II']
created: 2026-05-08 02:13:03
tree_path: Software > Page 0 > COCOMO Models Explained with Example Scenario A Un
---

COCOMO Models Explained with Example Scenario A University Management System (UMS) is to be developed to handle student admissions, faculty records, examinations, and result processing. The estimated size is 100 KLOC (Kilo Lines of Code) . 1. Intermediate COCOMO Definition: Intermediate COCOMO adds 15 cost drivers (e.g., reliability, complexity, team capability) to refine the effort estimate. Formula: Effort (PM) = a×(KLOC)b×EAF Development Time (TDEV) = c×(Effort)d Assumptions: •Project type: Semi-detached •Constants: a= 3.0,b= 1.12,c= 2.5,d= 0.35 •EAF (Effort Adjustment Factor): 1.15 Calculation: Effort = 3 .0×(100)1.12×1.15 ≈3.0×132.0×1.15≈455.4 PM TDEV = 2 .5×(455.4)0.35≈24.87 months 2. Detailed COCOMO Definition: Includes module-wise and phase-wise breakdown with specific cost drivers. Modules: •Admission: 40 KLOC, EAF = 1.10 •Exams: 30 KLOC, EAF = 1.25 1 •Reports: 30 KLOC, EAF = 1.05 Effort Estimation: Admission Effort = 3 .0×401.12×1.10≈162.4 Exams Effort = 3 .0×301.12×1.25≈144.8 Reports Effort = 3 .0×301.12×1.05≈121.5 Total Effort = 428 .7 PM Phase-wise Distribution: •Design: 20% ⇒85.74 PM •Coding: 45% ⇒192.91 PM •Testing: 25% ⇒107.18 PM •Integration: 10% ⇒42.87 PM 3. COCOMO II (Post-Architecture Model) Definition: A modern version that includes reuse, object-oriented development, and agile practices. Formula: Effort = A×SizeE×Y EM i Where E= 0.91 + 0 .01×Σ(Scale Factors) EM i–Individual Effort Multiplier (cost–driver rating). SFk–Scale Factor in COCOMO II Assumptions: •A = 2.94 •Size = 100 KSLOC •Σ Scale Factors = 18 ⇒E= 0.91 + 0 .18 = 1 .09 •QEM i= 1.25 Calculation: Effort = 2 .94×(100)1.09×1.25 ≈2.94×123×1.25≈452.6 PM 2

### Related Concepts
- [[Intermediate COCOMO]]
- [[UMS]]
- [[KLOC]]
- [[COCOMO II]]
- [[Detailed COCOMO]]
- [[COCOMO Models]]
