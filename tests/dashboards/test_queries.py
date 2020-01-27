def test_get_all_dashboards(client):
    assert {} == client.execute("""{
dashboards {
    edges {
      node {
        name
        description
        dateOfCreation
        creatorId
      }
    }
  }
}""")['data']
