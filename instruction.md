There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary to `/app/report.json`.

The report must be a single JSON object with exactly these keys:
`total_requests`, `unique_ips`, and `top_path`.

Success criteria:

1. `/app/report.json` exists and contains a valid JSON object.
2. `total_requests` equals the total number of request lines in the log.
3. `unique_ips` equals the number of distinct client IP addresses (the first field of each line).
4. `top_path` equals the request path that appears most frequently.
