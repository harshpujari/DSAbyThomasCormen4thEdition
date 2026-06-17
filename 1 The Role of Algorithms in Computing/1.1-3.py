'''
Hash Table (Dictionary/Map)

Strengths:
- O(1) average lookup time - Finding a value by key is nearly instantaneous, even with millions of entries
- Dynamic sizing - Automatically grows and shrinks as data is added/removed
- Flexible key types - Can use strings, numbers, or custom objects as keys
- Memory efficient - Only stores key-value pairs, no extra structural overhead like trees

Real-world strength example: A user authentication system checks if usernames exist in a database of 10 million users. A hash table returns results in microseconds, while a sorted array would require up to 23 comparisons using binary search.

Limitations:
- No ordering - Cannot iterate through data in sorted order without additional processing
- Hash collisions - Multiple keys can hash to the same location, degrading performance to O(n) in worst case
- Memory overhead - Requires extra space for hash buckets and typically maintains 70% capacity to avoid collisions
- Poor cache locality - Keys are scattered in memory, causing more cache misses than arrays

Real-world limitation example: An e-commerce site needs to display products sorted by price. A hash table storing product data by ID requires extracting all values and sorting them separately, while a balanced tree could return sorted results directly.

Best use case: When you need fast lookups by unique identifiers and don't require sorted iteration - like caching web requests, storing user sessions, or implementing database indexes.
'''