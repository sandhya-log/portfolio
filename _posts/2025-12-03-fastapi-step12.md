---
layout: step
project: fastapi-auth
step: 12
title: "Added JWT Tokens"
date: 2025-12-03
---


Today I implemented JWT tokens using PyJWT.

- Created access & refresh tokens
- Set expiry and refresh flow
- Wrote unit tests

```python
# sample code
from datetime import datetime, timedelta
