
import slugify
import pandas

print(f"This is the secfilecache module!")
print("\n Let's try some slugify things")
print(slugify("This is the secfilecache module!"))

print("\n Let's try some pandas things")
indentures = [{'a':1, 'b':2, 'c':3}, {'a':2, 'b':3, 'd':4}, {'a':6, 'b':6, 'c':7, 'e':None}]
df = pandas.DataFrame(indentures)
print(df)
print(type(df))