from behave import given, step, then

@given('eu tenho dois números inteiros: {num1:d} e {num2:d}')
def step_impl(ctx, num1, num2):
  ctx.num1 = num1
  ctx.num2 = num2

@step('eu somo os dois números inteiros')
def step_impl(ctx):
  ctx.soma = ctx.num1 + ctx.num2
