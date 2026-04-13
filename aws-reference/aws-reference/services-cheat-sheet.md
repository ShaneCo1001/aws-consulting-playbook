# AWS Services Cheat Sheet
*Plain English explanations for every major AWS service*

---

## Compute

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **EC2** | A virtual computer in the cloud | Always-on apps, long running processes |
| **Lambda** | Code that runs only when triggered | Short tasks, event driven, APIs |
| **ECS** | Runs Docker containers | Containerized apps, microservices |
| **Fargate** | Serverless containers (no servers to manage) | Containers without infrastructure hassle |
| **Elastic Beanstalk** | Deploy apps without managing infrastructure | Quick deployments, developers who don't want to configure AWS |

---

## Storage

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **S3** | Unlimited file storage in the cloud | Images, videos, backups, static websites |
| **EBS** | A hard drive for EC2 | EC2 storage, databases on EC2 |
| **EFS** | Shared file system multiple EC2s can access | Shared storage across multiple servers |
| **Glacier** | Very cheap archival storage | Long term backups, compliance data |

---

## Database

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **DynamoDB** | Fast NoSQL database | Simple key-value lookups, flexible schema |
| **RDS** | Managed SQL database (MySQL, PostgreSQL) | Complex relationships, reporting |
| **Aurora** | AWS's premium database (MySQL/PostgreSQL compatible) | High performance, enterprise workloads |
| **ElastiCache** | In-memory caching (Redis/Memcached) | Speed up database reads, session storage |
| **Redshift** | Data warehouse for analytics | Business intelligence, big data analysis |

---

## Networking

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **VPC** | Your own private network in AWS | Every production workload |
| **CloudFront** | CDN — serves content from nearest location | Websites, APIs, media delivery |
| **Route 53** | DNS — translates domain names to IPs | Custom domain names |
| **API Gateway** | Managed API front door | REST APIs, WebSocket APIs |
| **ELB** | Load balancer — distributes traffic | High availability, scaling |
| **NAT Gateway** | Lets private subnet reach internet | Private subnet internet access |

---

## Security

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **IAM** | Controls who can do what in AWS | Always — every AWS account |
| **Cognito** | User authentication for apps | Login/signup for web and mobile apps |
| **Secrets Manager** | Stores passwords and API keys securely | Database credentials, API keys |
| **WAF** | Web application firewall | Protect against web attacks |
| **Shield** | DDoS protection | High traffic websites |
| **KMS** | Encryption key management | Encrypting sensitive data |

---

## AI and ML

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **Bedrock** | Access to foundation AI models (Claude, Llama) | AI powered apps, chatbots |
| **SageMaker** | Build and train custom ML models | Custom AI models |
| **Rekognition** | AI image and video analysis | Face detection, content moderation |
| **Comprehend** | AI text analysis | Sentiment analysis, entity extraction |
| **Lex** | Build chatbots | Customer service bots, Alexa skills |
| **Polly** | Text to speech | Voice apps, accessibility |

---

## Messaging

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **SNS** | Send notifications (email, SMS, push) | Alerts, notifications, fan-out |
| **SQS** | Message queue for async processing | Decoupling services, batch processing |
| **EventBridge** | Event bus and scheduler | Scheduled tasks, event driven architecture |
| **Kinesis** | Real time data streaming | Live analytics, log processing |

---

## DevOps

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **CodePipeline** | Automated deployment pipeline | CI/CD orchestration |
| **CodeBuild** | Runs tests and builds code | Automated testing and building |
| **CodeDeploy** | Deploys to EC2 and Lambda | Automated deployments |
| **CloudFormation** | Infrastructure as Code | Reproducible infrastructure |
| **Amplify** | Full stack app hosting with CI/CD | React, Vue, Angular apps |

---

## Monitoring

| Service | Plain English | When To Use |
|---------|--------------|------------|
| **CloudWatch** | Logs, metrics, and alarms | Always — monitoring everything |
| **X-Ray** | Traces requests through your app | Debugging distributed systems |
| **CloudTrail** | Audit log of all AWS API calls | Security, compliance, debugging |
| **AWS Config** | Tracks configuration changes | Compliance, security auditing |

---

## Key Decision Frameworks

### SQL vs NoSQL
- Complex relationships or reporting → **RDS**
- Simple fast lookups, flexible schema → **DynamoDB**

### Lambda vs EC2 vs ECS
- Short tasks under 15 min → **Lambda**
- Always on, long running → **EC2**
- Containerized workloads → **ECS/Fargate**

### SNS vs SQS
- Fan out to multiple subscribers → **SNS**
- Queue for async processing → **SQS**
- Schedule tasks → **EventBridge**

### CloudFront vs API Gateway
- Static content (websites, images) → **CloudFront**
- Dynamic API calls → **API Gateway**
- Both together → **Common pattern!**