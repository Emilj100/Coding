 .replace(",", "").title().replace("/", " ").strip().split(" ")



    if x in month:
        x = month[x]
    if y in month:
        continue
    x = int(x)
    y = int(y)
    if x >= 13:
        continue
    if y >= 32:
        continue
    else:
        print(f"{z}-{x:02}-{y:02}")
        break
