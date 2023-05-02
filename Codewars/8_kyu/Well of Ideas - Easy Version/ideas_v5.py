def well(x):
    return (["Fail!"]+["Publish!"]*2+["I smell a series!"])[min(x.count("good"),3)]
