---
marp: true
theme: uncover
#class: invert
---

# Cloudless Testing of Serverless Applications

---

## Valtech Mobility

---

## One more tool for the backpack

Two Distinct things:

- Behavior Part
- Cloudless Part

---

## Lets build an application

### Car Descriptor

- Takes vehicle identification number (VIN)
- Create a text about that car

<!--
- Customer heard about AI
- Super Hot new thing
-->

---

## Behavior-Driven Design

- What should the software do?
  - Features
  - Contracts (Swagger)

<!--
The first thing you normally think about is:
- What is the thing I build supposed to do?
- I can see it in your heads that you are thinking about it.
-->

---

```gherkin
# generate_vehicle_descriptions.feature

Feature: Generate Vehicle Descriptions

    As a vehicle description service consumer
    I want to generate descriptions for vehicles
    So that I can provide comprehensive information to consumers.

    Scenario: Generate Description for Known Vehicle
        Given details about a specific vehicle are available
        And the AI description generator is functional
        When the user requests a description for this vehicle
        Then the Description Service provides a description for that vehicle
```

<!--
- "Given" as past
- "When" is present
- "Then" as near future

Respect the integrity of the step types: Givens set up initial state, Whens perform an action, and Thens verify outcomes. Don't arbitrarily reassign step types to make scenarios follow strict Given-When-Then ordering​1.

-->

<!--
Probably do that with your PO, or just done with the PO

- Similar to Arrange Act Assert
- Collection of Features

Main Point: You think about that anyway - just write it down

Use Business Language: Write Gherkin steps in the language that the business understands. Avoid technical jargon. The goal of BDD and Gherkin is to bridge the gap between the technical and non-technical stakeholders, so it's essential to keep the language accessible.

Start with the User's Goal: Every feature should start with a clear statement of the user's goal - what they're trying to achieve with this feature. This sets the context and makes the feature's purpose clear.

Keep Scenarios Independent: Each scenario should be independent and not rely on the state from other scenarios. This helps in ensuring that scenarios can be run individually without any dependencies.

Use Scenario Outline for Multiple Cases: If you have a scenario that needs to be run multiple times with different data, use a Scenario Outline. This allows you to define a template for the scenario and then provide a table of values to be used for each run.

Avoid too Many Steps: Keep the number of steps in each scenario to a minimum. Too many steps can make the scenario difficult to understand and maintain. As a rule of thumb, try to stick to Given-When-Then format without too many "And" steps.

Describe the Behavior, not the Implementation: The steps should describe what the system does, not how it does it. Avoid referring to specific clicks or UI elements in the steps. Instead, focus on the result of the action.

Use Background Wisely: The Background keyword allows you to specify steps that are common to every scenario in the feature. This can be useful for setup steps that are needed for each scenario. However, don't overuse this - if a step isn't necessary for the understanding of each scenario, it may be better to include it only in the scenarios that need it.

Refactor and Reuse Steps: Avoid duplication in your steps. If two steps are performing the same action but are worded differently, consider refactoring them into one step that can be used in both places.
-->

---

## Feature Test

![bg right height:500](assets/single-source-of-truth-256x256.png)

Gherkin

- Stakeholders love it
- POs love it
- PMs love it

Happy Cases
Unhappy Cases
control flow

---

### Gherkin Best Practices

1. Part of your codebase (can be refactored) <!-- e.g. unify steps definitions -->
2. Should be readable by anyone* <!-- strength is crossing from business to tech, use business terms, some technical details are ok -->
3. Behavior, not Procedures <!-- less like imperative tests, declarative rather than imperative ​-->
4. One Scenario, One Behavior
5. Hide irrelevant details  <!-- for that Behavior, especially when setting up given steps -->

---

## Steps

```text
cardescriptor/
    features/
        steps/
            descriptor.py
            openai.py
            vehicle_service.py
        environment.py
        generate_vehicle_descriptions.feature
```

<!--
- Many Languages possible
- Independent from application language
-> just use python
-->

---

```python
# environment.py
def before_all(context):
    context.app = httpx.Client(base_url="http://localhost:8080")
```

```python
# descriptor.py
@when("the user requests a description for this vehicle")
def request_description(context)
    context.response = context.app.get(f"/vehicle/{context.vin}/description")

@then("the Description Service provides a description for that vehicle")
def ensure_description(context)
    assert context.response.status_code == 200
    assert context.response.json()["vin"] == context.vin
    assert context.response.json()["description"]
```

<!--
- context.app -> Session to not repeat the base_url

-->

---

## Steps Best practices

- You can lie in your steps (Don't)
- If you think you need tests for your tests, you have gone too far

---

## Lets build it serverless

![height:500](assets/arch.png)

---

## Build for Production

- It should run in Production (The only thing everyone can agree on the only thing anyone can agree on) <!-- all tests is just to support this -->
- Likely several other stages
  - preprod/staging/tui
  - dev
- Continuous Integration Pipelines
  - probably many PR in parallel
- Many developers

---

## Non-negotiables

- no `if test`
- don't make changes to code to make it "testable"

## Negotiable

- Don't actually call external systems
- Mock external systems

---

## How to prevent conflicts?

- Each test run needs independent resources (especially databases & event distributors)

---

```python
# vehicle_service.py
@given("the Vehicle Service has information about a vehicle")
def setup_existing_vehicle(context)
    mock_existing_vehicle(context.vs, 200)
```

---

# Cloudless ?!

---

Docker Compose
- also a good way into serverless for K8S-ler

---

Wiremock

---

### Look at me, I'm microsoft now

```yaml
login.microsoftonline.com:
image: wiremock/wiremock
volumes:
    - ./build:/certs
    - ./features/mocks/oauth:/home/wiremock/mappings
command: "--disable-banner --global-response-templating --https-port 443 \
          --https-keystore /certs/oauth.p12 --keystore-password password"
```

```python
token = (
    ClientSecretCredential(tenant_id=..., client_id=..., client_secret=...)
    .get_token(scope=...).token
)
```

---

# Is this even a good Idea?

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
