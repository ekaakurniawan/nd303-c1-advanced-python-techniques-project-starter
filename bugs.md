# List of Bugs and the Fixes

1. [Fix printing error message](https://github.com/ekaakurniawan/nd303-c1-advanced-python-techniques-project-starter/commit/9ff2efa1e20406f52d939b5253762cf570eb38f6)
   - Print error message (Cannot load data, no filename provided) instead of class name (<class 'Exception'>)

2. [Fix error message that file not found](https://github.com/ekaakurniawan/nd303-c1-advanced-python-techniques-project-starter/commit/211ff1177294d700fbba03c9e8aeb157eec513f3)
   - Use `filename` variable as the result of the selection between user argument and default file name. Printing user argument will show None for default file name.

3. [Fix Unused Variable in verify_date Function](https://github.com/ekaakurniawan/nd303-c1-advanced-python-techniques-project-starter/commit/10498a06b960e268ffc5ef2265176808b6844e53)
   - Replace unused variable with underscore (`_`)

4. [Fix Duplicated DateSearch Name](https://github.com/ekaakurniawan/nd303-c1-advanced-python-techniques-project-starter/commit/e222e8313e986982f8a6ca5b1d055a03cf3dfb6e)
   - Rename DateSearch class into DateSearchType class as the name will be used in Query function.

5. [Rename Class Name QueryBuilder to Query](https://github.com/ekaakurniawan/nd303-c1-advanced-python-techniques-project-starter/commit/06e406ebefa31edf6185073a6f6ea0f452c1b979)
   - Some comments use class name QueryBuilder that should be Query
