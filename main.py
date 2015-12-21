from api_client import ApiClient

api_key = raw_input('Digite a chave da API: ')

base_url = raw_input('Digite url base da API: ')

api_client = ApiClient(api_key, 'categories', base_url)

print("Enviando request 'index'...\n")
print("Retorno: ")
print api_client.index()

print("\nEnviando request 'show'...\n")
print("Retorno: ")
print api_client.show(26)

params = {
  'category': {
    'name': 'a nova categoria'
  }
}

print("\nEnviando request 'create'...\n")
print("Retorno: ")
print api_client.create(params)

params = {
  'category': {
    'name': 'a nova categoria atualizada'
  }
}

print("\nEnviando request 'update'...\n")
print("Retorno: ")
print api_client.update(384, params)

print("\nEnviando request 'destroy'...\n")
print("Retorno: ")
print api_client.destroy(384)
