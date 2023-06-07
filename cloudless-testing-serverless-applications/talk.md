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

## Lets build and app

- What is it supposed to do?

-> Behavior

---

## Behavior-Driven Design with Cucumber

---

Acceptance Criteria

---

###

From the outside in

---

## Gherkin

Given when then

---

##

- PMs love id
- POs love it

Happy Cases
Unhappy Cases

control flow

---

## Steps

Swagger Contracts

Best practices

- If you think you need tests for your tests, you have gone too far


---

## Lets build it serverless

- Azure Function App
- Connects to other Services via https with AAD Token
- Cosmos DB
- KeyVault
- Storage Account

---

## Build for Production

really the only thing anyone can agree on

What problems do we want to solve

Non-negotiable

- no `if test`
- don't make changes to code to make it "testable"


---



---


# Cloudless ?!




## Stages

- prod
- staging/preprod/tui
- dev
- PRs
- Developers

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

