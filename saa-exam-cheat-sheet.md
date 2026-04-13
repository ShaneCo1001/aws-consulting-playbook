# AWS SAA Exam Cheat Sheet
*A comprehensive reference for common question patterns, decision frameworks, and key facts*

---

## How To Use This

When you see certain keywords in exam questions, they almost always point to a specific answer. This cheat sheet organizes everything by those patterns.

---

## The Big Keyword Patterns

| When you see... | The answer is usually... |
|----------------|------------------------|
| "Least operational overhead" | Most managed/serverless option |
| "Least expensive" | Spot > Reserved > Savings Plans > On-Demand |
| "Automatically scale" | Lambda + DynamoDB + S3 (serverless stack) |
| "Decouple services" | SQS or SNS |
| "Global users / low latency" | CloudFront + Route 53 Latency routing |
| "High availability" | Multi-AZ |
| "Fault tolerant" | Multi-Region |
| "Audit trail / compliance" | CloudTrail + Config + CloudWatch |
| "Temporary credentials" | STS + IAM Roles |
| "Encrypt data at rest" | KMS |
| "Encrypt data in transit" | TLS/SSL (HTTPS) |
| "Static website cheaply" | S3 + CloudFront |
| "Serverless architecture" | Lambda + API Gateway + DynamoDB |
| "Connect on-premises to AWS" | VPN (quick) or Direct Connect (consistent) |

---

## Compute — When To Use What

| Scenario | Service | Why |
|----------|---------|-----|
| Short tasks, unpredictable traffic | Lambda | Pay per execution, zero cost when idle, max 15 min |
| Always-on, long running, full OS control | EC2 | Persistent server, choose instance type |
| Containers, no server management | ECS with Fargate | Serverless containers, pay per task |
| Already using Kubernetes | EKS | Managed Kubernetes |
| Predictable workload, 1-3 years | Reserved Instances or Savings Plans | Up to 72% discount |
| Fault tolerant batch jobs | Spot Instances | Up to 90% cheaper, can be interrupted |

---

## Storage — When To Use What

| Scenario | Service | Why |
|----------|---------|-----|
| Files, images, backups at scale | S3 | Unlimited, pay per GB |
| Long-term archival, rarely accessed | S3 Glacier Deep Archive | Cheapest storage in AWS |
| High performance disk for EC2 | EBS (gp3 or io2) | Block storage attached to EC2 |
| Shared file system across EC2s | EFS | Managed NFS, scales automatically |
| Unpredictable access patterns | S3 Intelligent-Tiering | Auto-moves between tiers |

### S3 Storage Classes (cheapest to most expensive)
```
S3 Glacier Deep Archive → S3 Glacier → S3 One Zone-IA → S3 Standard-IA → S3 Standard
```

---

## Database — When To Use What

| Scenario | Service | Why |
|----------|---------|-----|
| Simple key-value, flexible schema, massive scale | DynamoDB | Single-digit ms latency, auto-scales |
| Complex relationships, SQL, ACID transactions | RDS | Managed SQL, automated backups |
| High performance SQL, enterprise | Aurora | 5x faster than MySQL, auto-scales storage |
| Speed up reads, session storage | ElastiCache Redis | Sub-ms latency, in-memory |
| Analytics, business intelligence | Redshift | Columnar storage, optimized for analytical queries |

### RDS Multi-AZ vs Read Replicas
| | Multi-AZ | Read Replicas |
|--|---------|--------------|
| Purpose | High availability (failover) | Scalability (read performance) |
| Replication | Synchronous | Asynchronous |
| Serves traffic? | No — standby only | Yes — serves reads |
| Cross-region? | No | Yes |

---

## Networking — When To Use What

| Scenario | Service | Why |
|----------|---------|-----|
| Serve content globally, low latency | CloudFront | CDN with 400+ edge locations, free HTTPS |
| HTTP/HTTPS load balancing, path routing | ALB | Layer 7, route by URL/host/headers |
| Ultra high performance, TCP/UDP, static IP | NLB | Layer 4, millions of requests/sec |
| Private subnet needs outbound internet | NAT Gateway | Managed, ~$0.045/hr, lives in public subnet |
| DNS, custom domains, health check failover | Route 53 | Multiple routing policies |
| Access S3/DynamoDB from private subnet free | VPC Endpoint | Gateway endpoints are free |

### Route 53 Routing Policies
| Policy | Use Case |
|--------|---------|
| Simple | Single resource, no health checks |
| Weighted | A/B testing, gradual traffic shifts |
| Latency | Route to lowest latency region |
| Failover | Active/passive failover |
| Geolocation | Route based on user's country/continent |
| Multi-value | Multiple healthy resources |

---

## Security — When To Use What

| Scenario | Service | Why |
|----------|---------|-----|
| Control who can do what | IAM roles and policies | Always roles over access keys |
| Store and rotate DB passwords/API keys | Secrets Manager | Auto-rotation built in |
| Encrypt data at rest | KMS | Integrates with S3, RDS, EBS, DynamoDB |
| Protect web apps from SQL injection, XSS | WAF | Works with CloudFront, ALB, API Gateway |
| DDoS protection | AWS Shield | Standard = free on CloudFront/Route 53 |
| User login/signup for apps | Cognito User Pools | Managed auth, JWT tokens, MFA |

### Security Groups vs NACLs
| | Security Groups | NACLs |
|--|----------------|-------|
| Level | Instance | Subnet |
| State | Stateful | Stateless |
| Rules | Allow only | Allow and Deny |
| Default inbound | Deny all | Allow all |
| Response traffic | Automatic | Need explicit outbound rule |

---

## Messaging and Decoupling

| Scenario | Service | Why |
|----------|---------|-----|
| Async processing, handle traffic spikes | SQS | Queue messages, Standard or FIFO |
| Send notifications to multiple subscribers | SNS | Pub/sub, fan-out pattern |
| Schedule tasks, event-driven | EventBridge | Cron schedules, AWS service events |
| Real-time data streaming | Kinesis | Retain 1-365 days, multiple consumers |

### SQS Standard vs FIFO
| | Standard | FIFO |
|--|---------|------|
| Delivery | At least once | Exactly once |
| Ordering | Best effort | Strict |
| Throughput | Unlimited | 300 msg/sec (3,000 with batching) |
| Use when | Maximum throughput | Order matters |

---

## High Availability and DR

| RTO/RPO | Strategy | Services |
|---------|---------|---------|
| Hours | Backup and restore | S3 backups, snapshots |
| 10s of minutes | Pilot light | Core services running, scale up on failure |
| Minutes | Warm standby | Scaled down version running in secondary region |
| Seconds | Multi-site active-active | Full capacity in multiple regions |

---

## Numbers You Must Memorize

### Lambda
- Max runtime: **15 minutes**
- Max memory: **10GB**
- Max package size: **250MB** unzipped
- Default concurrent executions: **1,000** per region

### S3
- Max object size: **5TB**
- Multipart upload required over: **100MB** (recommended)
- Bucket names: globally unique, lowercase, 3-63 chars

### RDS
- Backup retention: **0-35 days** (0 = disabled, default = 7)
- Multi-AZ failover time: **~60 seconds**
- Max read replicas: **5** (15 for Aurora)

### SQS
- Message retention: **1 minute to 14 days** (default = 4 days)
- Max message size: **256KB**
- Visibility timeout: **0 sec to 12 hours** (default = 30 sec)

### VPC
- /16 CIDR = **65,536 IPs**
- /24 CIDR = **256 IPs**
- AWS reserves **5 IPs** per subnet (first 4 + last 1)
- Max VPCs per region: **5** (soft limit, can increase)

### IAM
- Max policies per role: **10**
- Max access keys per user: **2**
- Password policy: configurable, MFA recommended

### CloudWatch
- Default metrics every: **5 minutes** (detailed = 1 minute)
- Log retention: **never expires by default** (set a policy!)
- Alarm evaluation: minimum **1 minute** periods

### EC2 Pricing Order (cheapest to most expensive)
```
Spot → Reserved (3yr all upfront) → Reserved (1yr) → Savings Plans → On-Demand → Dedicated
```

---

## Common Architecture Patterns

### Serverless API
```
User → CloudFront → API Gateway → Lambda → DynamoDB
```

### Highly Available Web App
```
Route 53 → ALB → EC2 (ASG, Multi-AZ) → RDS (Multi-AZ)
```

### Static Website
```
Route 53 → CloudFront → S3 (static hosting)
```

### Async Processing
```
API → Lambda → SQS → Lambda (processor) → DynamoDB
```

### Fan-out Pattern
```
Event → SNS → SQS Queue 1 → Lambda
              SQS Queue 2 → Lambda
              SQS Queue 3 → Lambda
```

### Secure Three-Tier Architecture
```
Internet → ALB (public subnet)
               → App servers (private subnet)
                   → RDS (private subnet)
Private subnet → NAT Gateway → Internet (outbound only)
```

---

## Migration Services Quick Reference

| Need | Service |
|------|---------|
| Migrate database with minimal downtime | DMS |
| Transfer petabytes — internet too slow | Snowball / Snowmobile |
| Online transfer from on-prem to S3/EFS | DataSync |
| Lift and shift EC2 workloads | AWS MGN (Application Migration Service) |
| Assess on-prem for migration | AWS Migration Hub |

---

## SAA Exam Tips

1. **"Least operational overhead"** always = most managed service (Lambda over EC2, Aurora Serverless over RDS, Fargate over ECS on EC2)
2. **Multi-AZ ≠ Multi-Region** — Multi-AZ = high availability, Multi-Region = disaster recovery
3. **Security Groups are stateful** — if you allow inbound, response is automatic
4. **NACLs are stateless** — need explicit rules for both directions
5. **S3 is not a file system** — use EFS for shared file storage across EC2
6. **NAT Gateway lives in public subnet, serves private subnet** — always
7. **CloudTrail = who did what, CloudWatch = what is happening**
8. **Reserved Instances save money on predictable workloads** — not for variable/unpredictable
9. **Spot Instances can be interrupted** — never use for critical always-on workloads
10. **Always use IAM Roles, never hardcode access keys in application code**

---

*Built from hands-on experience building a 24-service AWS application — Fantasy Sports Helper*
*Reference project: https://github.com/ShaneCo1001/Fantasy-Sports-Assistant*
