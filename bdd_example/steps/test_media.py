from behave import given, step, then

@given('eu tenho dois números inteiros: {num1:d} e {num2:d}')
def step_impl(ctx, num1, num2):
  ctx.num1 = num1
  ctx.num2 = num2

@step('eu somo os dois números inteiros')
def step_impl(ctx):
  ctx.soma = ctx.num1 + ctx.num2

@step('eu divido o resultado por 2')
def step_impl(ctx):
  ctx.resultado = ctx.soma / 2

@then('o resultado deve ser {resultado:d}')
def step_impl(ctx, resultado):
  assert ctx.resultado == resultado, f"Resultado incorreto. Esperado {resultado}. Obtido: {ctx.resultado}"

