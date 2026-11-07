---
title: "Model-driven engineering (IDM/MDA)"
collection: teaching
type: "Graduate course"
permalink: /teaching/2026-fall-model-driven-engineering
venue: "Ensias, Mohammed V University"
date: 2026-09-20
location: "Rabat, Morocco"
---

Model-driven engineering (IDM, *Ingénierie Dirigée par les Modèles*) puts models at the heart of software development: models are built, checked, transformed, and code is generated from them. This course covers metamodelling with EMF/Ecore, constraints with OCL, the OMG's Model-Driven Architecture (CIM, PIM, PDM, PSM), and the three ways of writing model transformations: by template (Acceleo), by programming (Java + EMF API) and by modelling (ATL).

## Description

Each notion is followed through a few familiar running examples: a traffic light (structure and state machine), a library (`Library`, `Book`, `Member`, `Loan`) followed from the requirements down to Java, Python and SQL code, an online shop, a company with departments and employees (OCL), and families (`Families2Persons`, ATL).

### Prerequisites

* Object-oriented design and UML 2 (class, object, use case and state diagrams)
* Object-oriented programming in Java
* Basics of relational databases and XML

### Tools

* JDK 17 or later
* [Eclipse Modeling Tools](https://www.eclipse.org/downloads/packages/) with EMF and Ecore Tools
* [Obeo Designer Community](https://www.obeodesigner.com/) / [Sirius](https://eclipse.dev/sirius/) (graphical editors)
* [Eclipse OCL](https://eclipse.dev/modeling/mdt/ocl/) (OCLinEcore, OCL console)
* [Acceleo 3.7](https://eclipse.dev/acceleo/) (update site: `https://download.eclipse.org/acceleo/updates/releases/3.7`)
* [ATL](https://eclipse.dev/atl/)

## Objectives

By the end of the course, students will be able to:

1. Explain what a model and a metamodel are, and place them in the OMG four-level architecture (M0–M3).
2. Define a metamodel with EMF/Ecore, generate its Java API and create conforming models (XMI) and graphical editors (Sirius).
3. Write OCL constraints (invariants, pre/post-conditions, derived attributes) and check a model against them.
4. Apply the MDA approach: move from requirements (CIM) to a platform-independent model (PIM), then to platform-specific models (PSM) and code.
5. Generate code (Java, Python, SQL) from a model with Acceleo templates.
6. Write a code generator in Java with the EMF API.
7. Write model-to-model transformations with ATL.
8. Choose the right transformation approach (template, programming or modelling) for a given problem.

## Course

Lectures are available as slides (in French), displayed in a read-only online viewer. The full course notes (in French, with numbered examples, exercises, quizzes and fully worked solutions, plus a syntax cheat sheet for OCL, Acceleo, the EMF API and ATL) will be available here: Course notes (PDF, *coming soon*).

|    | Lecture | Slides |
|:---|:--------|:-------|
| 1  | Introduction to model-driven engineering: models, metamodels and the OMG four-level architecture | [PDF](/viewer/?doc=MDE_Lecture1_2027) |
| 2  | Model-Driven Architecture (MDA): CIM, PIM, PDM, PSM and model transformations | [PDF](/viewer/?doc=MDA_Lecture2_2027) |
| 3  | Model-to-text transformation by template with Acceleo | [PDF](/viewer/?doc=Acceleo_Lecture3_2027_v2) |
| 4  | Transformation by programming (Java and the EMF API) | [PDF](/viewer/?doc=Programmation_Lecture4_2027) |
| 5  | Model-to-model transformation with ATL | [PDF](/viewer/?doc=ATL_Lecture5_2027) |

### Lecture contents

1. **Introduction to model-driven engineering** — why "coding first" no longer scales (cost of late errors, business rules scattered in the code), what a model is (representation, simplification, purpose), descriptive vs. prescriptive and contemplative vs. productive models, MDE: definition, benefits and limits, the OMG four-level stack (M0 real world, M1 model, M2 metamodel, M3 MOF/Ecore), "instance of" vs. "conforms to", conformance checking, the same stack in the UML, Java, XML and database worlds, Ecore and XMI.
2. **Model-Driven Architecture (MDA)** — separating the business from the platform, the formula *PIM + PDM ⇒ PSM ⇒ Code*, CIM (requirements), PIM (platform-independent solution with OCL constraints), PDM (platform description), PSM (Java/JPA and relational), traceability from requirements to code, the six MDA transformations (refinement, projection, migration, code generation, reverse engineering), taxonomy (endogenous/exogenous, horizontal/vertical, M2M/M2T/T2M), the three transformation approaches: by template (XSLT, Acceleo), by programming (Java + EMF) and by modelling (ATL, QVT).
3. **Code generation by template with Acceleo** — why generate code, the MOFM2T standard, structure of an Acceleo module (`[module]`, `[template]`, `@main`, `[file]`), navigating an Ecore model with OCL, `[for]` and separators, `[if]`, `[let]`, `[query]` (type mapping as a PDM), one file per class, protected areas, complete case study: generating Python classes, an SQL script (primary and foreign keys) and Java classes from `library.ecore`, common errors and good practices.
4. **Transformation by programming** — imperative vs. template-based generation, setting up a Java project with the EMF libraries, loading a model with a `ResourceSet`, from Ecore concepts to the EMF API (`getEClassifiers()`, `getEAttributes()`, `isMany()`, `isContainment()`), writing a generator step by step, `Library2Python`, `Library2SQL` and `Library2Java`, programmed protected areas, PyEcore, model-to-model by programming, template or programming?
5. **Model-to-model transformation with ATL** — M2M transformations and their place in MDA (PIM → PSM), structure of an ATL module (header, helpers, rules), matched rules (source pattern, filter, target pattern, bindings `<-`), operation and attribute helpers, the three execution phases and automatic resolution through the trace, the `Families2Persons` case study end to end in Eclipse, `Class2Relational`, rules with several target elements, lazy and called rules, common errors, ATL vs. Acceleo vs. Java.

### Course notes

The course notes, *Ingénierie Dirigée par les Modèles : du modèle au code*, follow the lectures and add two chapters on metamodelling with EMF/Ecore and on OCL, which are practised in the assignments and labs.

1. Introduction to model-driven engineering
2. Metamodelling with EMF and Ecore (EClass, EAttribute, EReference, containment, multiplicities, opposite references, inheritance, `.genmodel` and the generated Java API, XMI, Sirius editors)
3. The Object Constraint Language (OCL): context and `self`, navigation (1, 0..1, \*, reflexive associations, compositions), inheritance and type operations, collections and iterators, invariants, pre/post-conditions, `def`, `derive`, `init`, `body`, OCL at the metamodel level
4. Model-Driven Architecture (MDA)
5. Model-to-text transformation by template with Acceleo
6. Transformation by programming (Java and the EMF API)
7. Model-to-model transformation with ATL

Appendices: solutions to all exercises and quizzes; cheat sheet (OCL, Acceleo 3, EMF API, ATL) and glossary.

## Assignments (TD)

|    | Assignment | Link |
|:---|:-----------|:-----|
| 1  | Models and metamodels: the M0–M3 levels, conformance | [TD1](/viewer/?doc=TD_IDM_2027_M0_M3) |
| 2  | Model-Driven Architecture: from CIM to PSM | [TD2](/viewer/?doc=TD_MDA_2027) |
| 3  | Code generation with Acceleo (library case study) | [TD3](/viewer/?doc=TD_Acceleo_Library_2027) |
| 4  | MDA and Acceleo: combined exercises | [TD4](/viewer/?doc=TD_MDA_Acceleo_2027) |
| 5  | Transformation by programming with the EMF API (library case study) | [TD5](/viewer/?doc=TD_Programmation_Library_2027) |
| 6  | Model-to-model transformation with ATL: `Families2Persons` | [TD6](/viewer/?doc=TD_ATL_Families_2027) |

## Labs

Labs are done in Eclipse Modeling Tools.

|    | Lab | Link |
|:---|:----|:-----|
| 1  | Metamodelling with EMF/Ecore and Obeo Designer: build a metamodel, generate its Java API, create a model (`.xmi`) and a graphical editor | [Lab1](/viewer/?doc=TP_IDM_2027_EMF) |
| 2  | Viewpoint specification with Sirius: nodes, edges, styles and an editing palette | *coming soon* |
| 3  | Code generation with Acceleo from the `library.ecore` model (Java and SQL) | *coming soon* |
| 4  | Transformation by programming (Ecore → Python and Java code with the EMF API) | *coming soon* |
| 5  | Transformation by modelling with ATL: `Families2Persons` | *coming soon* |

## References

### Books

1. M. Brambilla, J. Cabot, M. Wimmer, *Model-Driven Software Engineering in Practice*, 2nd ed., Morgan & Claypool, 2017
2. D. Steinberg, F. Budinsky, M. Paternostro, E. Merks, *EMF: Eclipse Modeling Framework*, 2nd ed., Addison-Wesley, 2008
3. J. Warmer, A. Kleppe, *The Object Constraint Language: Getting Your Models Ready for MDA*, 2nd ed., Addison-Wesley, 2003

### Online resources

1. [OMG Model Driven Architecture](https://www.omg.org/mda/)
2. [Eclipse Modeling Framework (EMF)](https://eclipse.dev/modeling/emf/)
3. [Eclipse OCL](https://eclipse.dev/modeling/mdt/ocl/)
4. [Acceleo](https://eclipse.dev/acceleo/)
5. [ATL transformation language](https://eclipse.dev/atl/)
6. [Sirius](https://eclipse.dev/sirius/)
7. [PyEcore](https://github.com/pyecore/pyecore), EMF/Ecore for Python
