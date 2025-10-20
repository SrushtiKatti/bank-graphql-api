# Bank GraphQL API 

## Project Overview
This project implements a simple **Bank and Branch management system** using **Django** and **GraphQL** (`graphene-django`).  
It allows fetching bank branches along with their IFSC codes and associated bank names via GraphQL queries.

---

## Method Used
1. **Django Project & App**
   - Created a Django project (`bank_api_project`) and an app (`bank_api`).
2. **Models**
   - `Bank` model: Stores bank names.
   - `Branch` model: Stores branch names, IFSC codes, and linked to a bank via ForeignKey.
3. **GraphQL Schema**
   - Used `graphene-django` to define `BankNode` and `BranchNode`.
   - Implemented Relay-style queries for `banks` and `branches`.
4. **Sample Data**
   - Added sample banks (`State Bank of India`, `HDFC Bank`) and branches (`Sion Branch`, `Andheri Branch`).
5. **Testing**
   - Used Django `TestCase` and `graphene.test.Client` to validate GraphQL queries.

---

## Sample GraphQL Query

```graphql
query {
  branches {
    edges {
      node {
        branch
        ifsc
        bank {
          name
        }
      }
    }


## Sample Response
{
  "data": {
    "branches": {
      "edges": [
        {
          "node": {
            "branch": "Sion Branch",
            "ifsc": "SBIN0001234",
            "bank": { "name": "State Bank of India" }
          }
        },
        {
          "node": {
            "branch": "Andheri Branch",
            "ifsc": "HDFC0005678",
            "bank": { "name": "HDFC Bank" }
          }
        }
      ]
    }
  }
}

## Time Taken
Approximately **4 hours**.


  

