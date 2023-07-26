Warehouse Diagram
=================

A Warehouse has several loading bays and aisles, and each aisle has bins for
storing incoming goods.

```
Loading┌────┬───────────────────────────────┬───┐
   ────┼──► │                               │   │
 Bay   │    └───────────────────────────────┘   │
       │                                        │
       │                                        │
  Bin  │    ┌──────┐     ┌──────┐    ┌──────┐   │
    ───┼────┤►O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
  Aisle│    │ O  O │     │ O  O │    │ O  O │   │
    ───┼───►│      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    │      │     │      │    │      │   │
       │    │ O  O │     │ O  O │    │ O  O │   │
       │    └──────┘     └──────┘    └──────┘   │
       │                                        │
       └────────────────────────────────────────┘
```
