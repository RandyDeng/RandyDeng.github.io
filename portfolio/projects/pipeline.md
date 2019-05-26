---

layout: portfolio_page
background: portfolio
title: Pipelined Microarchitecture

---

The LC-3b simulator is a C program that implements a 5-stage piplined microarchitecture of the LC-3b ISA. The simulator itself is a modified version of Professor Yale Patt's course at UT Austin, but the functionality of each piplined stage was coded solely by myself. Programming the simulator required thorough knowledge of the ISA as well as proper organization of code. For example, the pipeline code cannot run each stage of the pipeline in parallel. Instead, the code must account for this by processing later stages first. This application could be easily extended to take into account virtual memory, caching, and more.
