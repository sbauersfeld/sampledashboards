def sumRows(data):
  data['sum'] = data.sum(axis=1)
  return data