---
layout: step
title: "Step 12 — Added JWT Tokens"
project: fastapi-auth
category: coding
date: 2025-12-03
---

Today I implemented JWT tokens using PyJWT.

- Created access & refresh tokens
- Set expiry and refresh flow
- Wrote unit tests

```python
# sample code
from datetime import datetime, timedelta
