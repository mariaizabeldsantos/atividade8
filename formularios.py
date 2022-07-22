25 linhas (21 sloc)  1,21 KB
class Formulario ( FlaskForm ):
    altura = FloatField ( 'altura' , validadores = [ DataRequired()])
     largura = FloatField ( 'largura' , validadores = [ DataRequired()])
    tipoCortina = SelectField ( u'Tipo Curtina ' , options = [( 'oxford' , 'Oxford' ), ( 'tergal' , 'Tergal' ), ( 'gabardine' , 'Gabardine' )])

@aplicativo. _ rota( "/" , métodos = [ "GET" , "POST" ])
def casa ():
    formulario = formulario()
    se formulario. validate_on_submit():
        largura = formulario . largura. dados
        altura = formulario . altura. dados
        tipoCortina = formulario . tipoCortina. dados
        metro_quadrado = altura * largura
        preço = 0
        if (tipoCortina == "oxford" ):
            preco = metro_quadrado * 83
       
        if (tipoCortina == "tergal"):
            preco = metro_quadrado * 62
        
        if ( tipoCortina == "gabardine" ):
            preco = metro_quadrado * 105
            
        return "<h2>Resultado da pesquisa:</h2>" + "<p>O orçamento da cortina tipo </p>" + tipoCortina . format() + "é de <b>R$" + str(preco)
    return render_template('home.html', form = formulario)