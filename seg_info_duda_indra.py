import hashlib

myText = []

myText.append('A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.')
myText.append('A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus')
myText.append('Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.')
myText.append('A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.')
myText.append('Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982')
myText.append('Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.')
myText.append('O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.')
myText.append('Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.')
myText.append('Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.')
myText.append('Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.')


for i in range (0,9):
    SHA256 = hashlib.sha256(myText[i].encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText[i].encode('utf-8')).hexdigest()
    
    print("\"" +myText[i] + "\" - " + SHA256 + " - " + MD5)



