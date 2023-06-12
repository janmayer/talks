---
marp: true
theme: uncover
#class: invert
style: |
  .small-text {
    font-size: 0.5rem;
  }
---

# Cloudless Testing of Serverless Applications

TODO: Jan Mayer

---

## Valtech Mobility

TODO: Slide about VM

---

![bg](assets/cloud_toolbelt.png)

<!--
I want to give you two more tools for your toolbelt in your cloud journey
- Behavior
- Cloudless
-->

---

## Behavior-Driven Design

---

### New requirement: <br> Car Descriptions

> So, we need a detailed description for individual cars to display on the frontend and in our PDFs for vendors. The cars are highly customizable, so we every description will be different.

<!--
- Customer heard about AI
- Super Hot new thing
-->

---

### What Should the Software Do?

- What features should the software have?
  - Features & Acceptance Criteria
- How should the software interact with other systems?
  - Contracts (Swagger API)
- What should the user experience look like?

<!--
The hardest single part of building a software system is deciding precisely what to build.

The first step in any software development project is to define the behavior.
- I can see it in your heads that you are thinking about it.
- A lot of time is spend figuring out what exactly is it that the end result should do
- You are thinking about those anyway - write them down

Features & Acceptance Criteria
- The "what" of the software - what should it do?
- Defined by project stakeholders and developers together.
- Drives the development process and provides a clear goal to aim for.

Contracts (Swagger API)
- The "how" of interaction between software components
- Defines how software will interact with other systems.
- Can be thought of as the "language" that systems use to communicate with each other.
-->

---

> The hardest single part of building a software system is deciding precisely what to build.

<p style="font-size: 75%; text-align:right">- Fred Brooks</p>

---

### Write it down ...

```gherkin
# features/generate_vehicle_descriptions.feature

Feature: Generate Vehicle Descriptions

    As a vehicle description service user
    I want to generate descriptions for vehicles
    So that I can provide comprehensive information to customers.

    Scenario: Generate Description for Known Vehicle
        Given details about a specific vehicle are available
        And the AI description generator is functional
        When the user requests a description for this vehicle
        Then the Description Service provides a description for that vehicle
```

<!--
You and the PO go and discuss this with the customers, and the come up with this.

- "Given" as past
- "When" is present
- "Then" as near future

Respect the integrity of the step types: Givens set up initial state, Whens perform an action, and Thens verify outcomes. Don't arbitrarily reassign step types to make scenarios follow strict Given-When-Then ordering​1.
-->

---

### .. and automate it

```python
# features/steps/steps.py

@when("the user requests a description for this vehicle")
def request_description(context)
    context.response = requests.get(
        f"http://localhost:8080/vehicles/{context.vin}/description"
    )

@then("the Description Service provides a description for that vehicle")
def ensure_description(context)
    assert context.response.status_code == 200
    assert context.response.json()["vin"] == context.vin
    assert context.response.json()["description"]
```

<!--
Ideally, also test against the swagger

Notice "Description" is not well defined
-->

---

![height:500](assets/single-source-of-truth-256x256.png)

<https://cucumber.io/docs/>

<!--
Stakeholders, Product Owners (POs), and Project Managers (PMs) love Gherkin Feature Tests

- Stakeholders love it
- Happy Cases & Unhappy Cases

### Behavior-Driven Design (BDD)

- Methodology for developing software based on its expected behavior
- Starts with a clear understanding of behavior and works backward to implement it
- Encourages collaboration between tech and non-tech stakeholders

BDD is a way for software teams to work that closes the gap between business people and technical people by:

- Encouraging collaboration across roles to build shared understanding of the problem to be solved
- Working in rapid, small iterations to increase feedback and the flow of value
- Producing system documentation that is automatically checked against the system’s behaviour

-->

---

### Feature Tests Best Practices

1. Part of your codebase (can be refactored!) <!-- e.g. unify steps definitions -->
2. Should be readable <!-- strength is crossing from business to tech, use business terms, some technical details are ok -->
3. Behavior, not Procedures <!-- less like imperative tests, declarative rather than imperative ​-->
4. One Scenario, One Behavior
5. Hide irrelevant details  <!-- for that Behavior, especially when setting up given steps -->

---

### Automation Steps Best Practices

1. Try not to lie in your steps
2. You can take shortcuts in steps <!-- write directly to the database -->
3. If you think you need tests for your tests, <br> you have gone too far

---

## Serverless

![bg](assets/serverless.png)

<!--
- So far, completely technology agnostic
-->

---

![height:400](assets/arch.png)

---

### Build for Production

- It should run in Production <!-- (The only thing everyone can agree on the only   thing anyone can agree on),  all tests is just to support this -->
  - no `if $test`
  - no changes to code to make it "testable"
- should also run on
  - several other stages
  - Continuous Integration Pipelines
    - probably many PR in parallel
  - Locally for developers

<!--
- The only thing everyone can agree on the only thing anyone can agree on)
- all tests are just to support this
<!--
- Likely several other stages
  - preprod/staging/tui
  - dev
-->

---

## Problems when testing

1. How to handle many parallel test runs?

  - Continuous Integration Pipelines <!-- probably many PR in parallel -->
  - Many developers <!-- should they all have their -->
  - Each test run needs independent resources (especially databases & event distributors)

2. How to test failure cases?
  - Can't force real external services to fail
  - Mock external systems <!-- Don't actually call external systems -->

<!--
TODO: Illustration

- Each test run needs independent resources
- (especially databases & event distributors)
- Don't actually call external systems
- Mock external systems

-->

---

## Cloudless?

![bg](assets/cloudless.png)

---

### Run Azure Functions locally

TODO: Live Demo

---

### Docker Compose

- also a good way into serverless for K8S-ler

---

### Wiremock

---

## Recap

-
- It's all http? Always has been. Wiremock

---

## Is this even a good Idea?

Understand why you are doing something

- A lot of work
- ... ensures continuous testing
- ... language and infrastructure agnostic
    - supports transition from and to other systems
- ... you know better what your code does
    - but do you want to know that?
- ... allows for the ultimate flex when refactoring

Ideally 100% coverage (for real this time)
Delete Something and see what breaks

Unit Test -> Concrete
Outside Harder, Inside Softer


---

VENN

Unittests : Behaviourtests : "Integration"tests : E2E tests


Micro -> Macro


---

# Key Takeaways

- BDD: You are doing it anyway - just write it down
- Cloudless testing allows for continuous testing independent of cloud resources
- Tools like Docker Compose and WireMock help us create isolated testing environments and realistic mock responses
- It requires significant effort to set up, but can be very beneficial in the long run

---
