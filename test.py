import termseparator as ts


# 1. Simple, default usage (green solid line)
ts.s()

# 2. Separator with a centered title (default green)
ts.s("DATA LOADING COMPLETE")

# 3. Separator with a different color
ts.s("PROCESSING DATA", color="blue")

# 4. Solid red line
ts.s(color="red")