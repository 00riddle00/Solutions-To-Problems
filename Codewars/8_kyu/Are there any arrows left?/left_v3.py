def any_arrows(arrows):
    return 1-all(a.get("damaged") for a in arrows)
