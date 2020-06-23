# How to use

```
Run counter.py
Enter absolute path to directory
Add all extensions to read (.py, .js, .css etc.), type end when finished
Add any files to ignore (exceptions):
  File: Enter filename (no extension)
  Folder: Enter folder name + / (e.g. node_modules/)

Add any templates, which are in filters.py:
  django: ignores settings, manage, migrations etc.
          searches for .py, .js, .css and .html
  
  vue:    ignores node_modules/, dist/
          searches for .js, .vue
```
