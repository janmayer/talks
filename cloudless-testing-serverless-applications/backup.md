---
marp: true
theme: uncover
#class: invert
---

### Feature Tests Best Practices

1. Part of your codebase (can be refactored!) <!-- e.g. unify steps definitions -->
2. Use the right words <!-- strength is crossing from business to tech, use business terms, some technical details are ok -->
3. Behavior, not Procedures <!-- less like imperative tests, declarative rather than imperative ​-->
4. One Scenario, One Behavior
5. Hide irrelevant details  <!-- for that Behavior, especially when setting up given steps -->

---

### Automation Steps Best Practices

1. Try not to lie in your steps
2. You can take shortcuts in steps <!-- write directly to the database -->
3. If you think you need tests for your tests, <br> you have gone too far

---