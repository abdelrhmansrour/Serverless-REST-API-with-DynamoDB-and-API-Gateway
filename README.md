# 📝 Serverless To-Do List App (AWS API Gateway + Lambda + DynamoDB)

This project is a simple, fully serverless to-do list application using:

- **Amazon API Gateway** – Exposes RESTful endpoints
- **AWS Lambda** – Handles CRUD operations
- **Amazon DynamoDB** – Stores to-do records
- **Amazon S3** – Hosts the frontend (HTML + JS)
- **Amazon CloudWatch** – Logs API activity
- **AWS IAM** – Secures access

---

## 📌 Architecture Diagram

<img width="1253" height="748" alt="image" src="https://github.com/user-attachments/assets/a578cb01-e47f-4b81-a166-86c21568505c" />
 
    
    https://lucid.app/lucidchart/9582c622-ce90-47b9-b871-a5102cdafd43/edit?viewport_loc=55%2C51%2C2124%2C1069%2C0_0&invitationId=inv_b9a3cf74-cfb4-44fb-a763-38bb64cadbf1
---

## 🚀 Features

- ✅ Add, read, update, delete tasks
- ✅ REST API powered by API Gateway + Lambda
- ✅ Fully serverless (no EC2 or backend server)
- ✅ Frontend hosted on S3
- ✅ CORS-configured for browser access
- ✅ Free-tier friendly (fully within AWS free tier)

  
---

## 🛠 Setup Instructions

### 1. **Deploy the Backend**

- Create a DynamoDB table:
  - Table name: `TodoList`
  - Primary key: `id` (string)
- Create 4 Lambda functions:
  - `CreateTask`, `GetTasks`, `UpdateTask`, `DeleteTask`
  - Assign execution role with access to DynamoDB
- Create an **API Gateway REST API**
  - Add resources and methods for each Lambda function
  - Enable **CORS** for all methods (including `OPTIONS`)
  - Deploy to stage: `dev`

### 2. **Frontend Hosting**

- Upload `index.html` and `app.js` to an S3 bucket
- Make the bucket public (or use CloudFront)
- Ensure CORS is enabled on the API

---

## 🔌 API Endpoints

| Method | Endpoint                | Description       |
|--------|-------------------------|-------------------|
| POST   | `/tasks`                | Create a task     |
| GET    | `/tasks`                | Get all tasks     |
| PUT    | `/tasks/{id}`           | Update a task     |
| DELETE | `/tasks/{id}`           | Delete a task     |

---

## ✅ TODOs

-  Lambda functions with CRUD logic
-  REST API with CORS enabled
-  Frontend with fetch() calls
-  Public GitHub repo with diagram and docs ✅

---

