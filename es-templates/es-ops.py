from __future__ import print_function
import curator
import elasticsearch as es
from elasticsearch import Elasticsearch


HOSTS = ['command.tlr.io']
PORT = 9200
SNIFF = False
TIMEOUT = 120

hosts = ['{}:{}'.format(h, PORT) for h in HOSTS]

client = Elasticsearch(hosts=hosts,
                       sniff_on_start=SNIFF,
                       sniff_on_connection_fail=SNIFF,
                       timeout=TIMEOUT)
idx_client = es.client.IndicesClient(client)
snap_client = es.client.SnapshotClient(client)
cluster_client = es.client.ClusterClient(client)
nodes_client = es.client.NodesClient(client)


def indices(connection=client):
    return curator.get_indices(connection)


def aliases(connection=client):
    return {v['aliases'].keys()[0]: k for k, v in connection.indices.get_aliases().items() if v['aliases']}  # noqa


def index_get_mapping(index_client=idx_client, index='stoploggingtoyourdbcom-1'):  # noqa
    return index_client.get_mapping(index)


def index_get_settings(index_client=idx_client, index='stoploggingtoyourdbcom-1'):  # noqa
    return index_client.get_settings(index, human=True)


def index_get_segments(index_client=idx_client, index='stoploggingtoyourdbcom-1'):  # noqa
    return index_client.segments(index, human=True)


def index_get_stats(index_client=idx_client, index='stoploggingtoyourdbcom-1'):
    return index_client.stats(index, human=True)


def indices_close(connection, indices):
    curator.close_indices(connection, indices)
    if isinstance(indices, (list, tuple)):
        return ' '.join([', '.join(indices), 'closed'])
    else:
        return ' '.join([indices, 'closed'])


def indices_open(connection, indices):
    curator.open_indices(connection, indices)
    if isinstance(indices, (list, tuple)):
        return ' '.join([', '.join(indices), 'opened'])
    else:
        return ' '.join([indices, 'opened'])


def indices_delete(connection, indices):
    curator.delete_indices(connection, indices)
    if isinstance(indices, (list, tuple)):
        return ' '.join([', '.join(indices), 'deleted'])
    else:
        return ' '.join([indices, 'deleted'])


def indices_value_filter(filter_type='prefix', filter_value='.marvel'):
    """
    valid filter types are prefix, suffix, exclude, and regex
    """
    return curator.build_filter(kindOf=filter_type, value=filter_value)


def indices_date_filter(filter_type='older_than', filter_value=30,
                        time_unit='days', timestring='%Y.%m.%d'):
    """
    valid filter types are older_than and newer_than
    time unit could be days, months, or years.
    """
    return curator.build_filter(kindOf=filter_type, value=filter_value,
                                time_unit=time_unit, timestring=timestring)


def indices_apply_filter(indices, filter):
    return curator.apply_filter(indices, **filter)


def cluster_settings(cluster=cluster_client):
    return cluster.get_settings()


def cluster_health(cluster=cluster_client, level='cluster'):
    """ valid level choices are
        cluster
        indices
        shards
    """
    return cluster.health(level=level)


def cluster_pending_tasks(cluster=cluster_client):
    return cluster.pending_tasks()


def cluster_state(cluster=cluster_client, indices='_all'):
    """ indices can be comma seperated, eg, indices='stoploggingtoyourdbcom-1' # noqa
    """
    return cluster.state(index=indices)


def cluster_stats(cluster=cluster_client):
    return cluster.stats(human=True)


def node_hot_threads(nodes=nodes_client):
    return nodes.hot_threads()


def node_info(nodes=nodes_client):
    return nodes.info(human=True)


def node_stats(nodes=nodes_client, level='node'):
    """
    valid level choices are
    node
    indices
    shards
    """
    return nodes.stats(human=True, level=level)
