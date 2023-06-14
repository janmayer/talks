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

### BDD and cloudless go well together

* ensures continuous testing
* ultimate flexibility when refactoring
* language and infrastructure agnostic
* supports transition from and to other systems
* you know better what your code does

<!--
Ideally 100% coverage (for real this time)
Delete Something and see what breaks

Unit Test -> Concrete
Outside Harder, Inside Softer
No silver bullet
-->

---

## Key Takeaways

- BDD: You are doing it anyway
- Cloudless testing allows for continuous testing independent of cloud resources
- Tools like Docker Compose and Wiremock help us create isolated testing environments and realistic mock responses
- It requires significant effort to set up, but can be very beneficial in the long run

<!--
- also a good way into serverless for K8S-ler
-->

---

Ideally 100% coverage (for real this time)
Delete Something and see what breaks
* supports transition from and to other systems
* you know better what your code does

Unit Test -> Concrete
Outside Harder, Inside Softer
No silver bullet

---

- BDD: You are doing it anyway
- Cloudless testing allows for continuous testing independent of cloud resources
- Tools like Docker Compose and Wiremock help us create isolated testing environments and realistic mock responses
- It requires significant effort to set up, but can be very beneficial in the long run

- also a good way into serverless for K8S-ler
