---
marp: true
theme: uncover
#class: invert
style: |
  .icon {
    display: inline-block;
    width: 1em;
    height: 1em;
    background-size: cover;
    vertical-align: middle;
  }

  .icon-linkedin {
    background-image: url('assets/linkedin.svg');
    margin-top: -10px;
  }

  .icon-github {
    background-image: url('assets/github.svg');
    margin-top: -10px;
  }

  h1 {
    font-size: 170%;
  }
---

# Cloudless Testing of Serverless Applications

### Dr. Jan Mayer

[jan.mayer@valtech-mobility.com](mailto:jan.mayer@valtech-mobility.com)

<i class="icon icon-github"></i> [janmayer](https://github.com/janmayer) | <i class="icon icon-linkedin"></i> [dr-jan-mayer](https://www.linkedin.com/in/dr-jan-mayer/)

![bg left:25%](assets/jan-mayer-bg.svg)

---

![bg](assets/cloud-journey.png)

<!--
My goal is to give you more tools you can put in your backpack
and at some point in your cloud journey you can pull them out
and say: Yep, that is the right tool for this.
-->

---

> The hardest single part of building a software system is deciding precisely what to build.
<p style="font-size: 75%; text-align:right">- Frederick Brooks, 1987</p>

<!--
https://www.cgl.ucsf.edu/Outreach/pc204/NoSilverBullet.html

Some of you might know this quote:
The hardest single part of building a software system is deciding precisely what to build.
Its from 1987 - so that problem has been known for longer than I am alive.
-->

---

> The hardest single part of building a software system is deciding precisely what to build.
<p style="font-size: 75%; text-align:right">- Frederick Brooks, 1987</p>

<br>

> The second hardest part is keeping the documentation in sync with reality.
<p style="font-size: 75%; text-align:right">- me, now</p>

<!--
And to that I might jokingly add:
he second hardest part is keeping the documentation in sync.
-->

---

## Behavior-Driven Development

You are already doing it.

<!--
The first step in any software development project is to define the behavior.
-->

---

### Behavior?

* **Who** & **Why**: User Experience
* **How**: Contracts (Boundaries, Interfaces)
* **What**: Features (Acceptance Criteria)

<!--
User Experience
- The "Who" - Who the users of the system are, designing the system with a focus on the user's needs, expectations, and context.
- The "Why" - Why the system is being developed, ensuring that the software is meaningful and valuable to the users.

Contracts (Swagger API)
- The "how" of interaction between software components
- Defines how software will interact with other systems.
- Can be thought of as the "language" that systems use to communicate with each other.

Features & Acceptance Criteria
- The "what" of the software - what should it do?
- Defined by project stakeholders and developers together.
- Drives the development process and provides a clear goal to aim for.
-->

---

### New requirement: <br> Car Descriptions

> We need a detailed description for individual cars <br> to display on the frontend and in our PDFs for vendors. The cars are highly customizable, so
every description will be different.

<!--
- Let's consider an Example I made up for this talk
- Customer heard about AI
- Super Hot new thing
...
-->

---

### Formalize Features ...

```gherkin
# features/generate_vehicle_descriptions.feature (Gherkin)

Feature: Generate Vehicle Descriptions

    As a vehicle description service user
    I want to generate descriptions for vehicles
    So that I can provide comprehensive information to customers.

    Scenario: Generate description for known vehicle
        Given details about a specific vehicle are available
        And the AI description generator is functional
        When the user requests a description for this vehicle
        Then a description for this vehicle is provided
```

<!--
You and the PO go and discuss this with the customers, and the come up with this.

Cucumber is a tool that supports BDD
It uses plain language specifications (Gherkin language) to define behavior
This simplifies communication, facilitates collaboration and fosters a shared understanding.

- Given: The initial context or preconditions required for the scenario to be valid. It sets up the starting point for the behavior being described.
- When (only 1x): The specific action or event that triggers the behavior. It represents the stimulus or input that leads to the expected outcome.
- Then: The expected outcome or behavior that should result from the given context and action. It represents the observable results or state changes in the system.
-->

---

### ... and automate

```python
# features/steps/steps.py (Python)

@when("the user requests a description for this vehicle")
def request_description(context):
    context.response = requests.get(
        f"http://localhost:8080/vehicles/{context.vin}/description"
    )

@then("a description for this vehicle is provided")
def ensure_description(context):
    assert context.response.status_code == 200
    assert context.response.json()["vin"] == context.vin
    assert context.response.json()["description"]
```

<!--
Steps are what translates the plain text to actual code

-> From the outside in
Here,
- user requests means "GET"
- and vehicle means with a VIN

provides a description means
- ...
- Ideally, also test against the swagger
- Notice "Description" is not well defined
-->

---

### Benefits

* Collaboration
* Clarity
* Testability
* Documentation

![bg right:38.2% height:450](assets/single-source-of-truth-256x256.png)

<p style="font-size: 50%; bottom:50px; right:0px; position:absolute">https://cucumber.io/docs/</p>


<!--
Collaboration:
  - Enhances communication: Promotes shared understanding among roles.
  - Stakeholders, Product Owners (POs), and Project Managers (PMs) love this
  - Better understanding and knowledge sharing

Clarity:
  - Reduces misunderstandings and promotes clearer expectations before coding
  - focus on what the system should do, not how
  - Ensures business-value focus: Encourages building features that matter to users.

Testability:
  - Ensures system behavior can be automatically tested and verified,
  - regardless of the underlying implementation.

Documentation:
  - Provides up-to-date, executable, and implementation-agnostic specifications.
-->

---

### Recommendations

* Part of your codebase (can be refactored!)
* Not an exact science
  * Strive for symmetry
  * Hide irrelevant details
  * Consider shortcuts
* If need tests for your tests, you have gone too far

<!--
- Refactor when knowledge about your system increases

French Poetry 18th Century
- less like imperative tests, declarative rather than imperative
- hide for that Behavior, keep some technical details
- consider writing directly to the database

...
-->

---

## Serverless

![bg](assets/serverless.png)

<!--
- So far, completely technology agnostic
-->

---

## Implementation on Azure

![height:400](assets/arch.png)

---

### Building for Production

* It should run in Production
  * No `if $test`
  * No changes to code to make it "testable"
* Should also run on
  * Several other stages
  * Continuous Integration pipelines
  * Locally for developers

<!--
Production
- only thing everyone can agree on the only thing anyone can agree on
- all tests is just to support this

...

- Likely several other stages
  - preprod/staging/tui
  - dev

- probably many PR in parallel
-->

---

### Problems when Testing

* Developer Experience
  * Needs to be *fast*
* Continuous Integration
  * Might compete for resources
  * Deploy every run to the cloud !?
* External Systems
  * Can't test failure cases with live systems

<!--
  * Need mock external systems
TODO: Illustration
  Don't actually call external systems
  - Many developers should they all have their
  - Each test run needs independent resources (especially databases & event distributors)
- Each test run needs independent resources
- (especially databases & event distributors)
- Don't actually call external systems
- Mock external systems
-->

---

## Cloudless

![bg](assets/cloudless.png)

---

### Local Development Demo

<!--
### Local Development

- Docker Compose
- Azure Functions Container
- Wiremock for everything http

![bg right height:300](assets/arch.png)
-->

---

### Local Replacements

<style scoped>table {font-size: 75%;}</style>

| Azure                          | Docker   |
| -----------------------------: | :------- |
| Function App                   | azure-functions (Official)
| AD, Key Vault, Management, ... | Wiremock |
| Storage Account                | Azurite (Official)  |
| Cosmos DB                      | Cosmos DB Emulator (Official), cosmosdb-server |
| Event Grid                     | azureeventgridsimulator   |
| Event Hub                      | ?, (Kafka) |
| Service Bus                    | ?, (RabbitMQ) |

<!--
https://jimmybogard.com/local-development-with-azure-service-bus/
https://feedback.azure.com/d365community/idea/39679808-7626-ec11-b6e6-000d3a4f032c
-->

---

### No Silver Bullet

* Infrastructure & Security
  * Deploy to Dev
  * Test Suite for Security
* Integration
  * (E2E) Happy Cases
  * Health Monitoring
* Performance
  * Load Testing

![bg right:38.2%](assets/computer-clouds-tools.png)

---

### BDD + Cloudless = ❤️

* You are already doing BDD
  * Language & infrastructure agnostic
  * Ultimate flexibility when refactoring
* Cloudless environments
  * Fast iteration locally
  * Better CI pipelines

![bg right:38.2%](assets/cloud-toolbelt.png)
