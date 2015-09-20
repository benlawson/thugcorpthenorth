import core, indico
def run_clusters(latitude, longitude, dis, topic):
    cc = core.client_choice(latitude, longitude, dis, topic)
    fc = indico.filtered_clusters()

    matches = core.compare_clusters(cc, fc)
    return matches
