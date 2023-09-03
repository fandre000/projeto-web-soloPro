from django.shortcuts import render, redirect

from .models import Pessoa, Candidato, Vaga




def index(request):
    
    return render(request, 'home/index.html')




def login(request):

    return render(request, 'home/login.html')




def detalhes(request):

    return render(request, 'home/detalhes.html')




def candidatos(request):
  
    return render(request, 'home/candidatos.html', { 

        'candidatos': Candidato.objects.all()


    })

    return render(request, 'home/candidatos.html')




def exemplo(request):
    
    return render(request, 'home/exemplo.html')




def vagas(request):
    vagas = { 

        'vagas': Vaga.objects.all()


    }

    return render(request, 'home/vagas.html', vagas)




def teste(request):

    pessoas = Pessoa.objects.all()

    return render(request, 'home/teste.html', {"pessoas": pessoas})




def admin(request):

    return render(request, 'admin/teste.html')



def salvar(request):

    pessoa = Pessoa()

    pessoa.nome = request.POST.get("nome")


    pessoa.endereco = request.POST.get("endereco")
    


    pessoa.idade = request.POST.get("idade")
    

    pessoa.save()
  

    pessoas = Pessoa.objects.all()  

    return render(request, 'home/teste.html', {"pessoas": pessoas})





def editar(request, id):

    pessoa = Pessoa.objects.get(id = id)


    return render(request, 'home/update.html', {"pessoa": pessoa})


def update(request, id):

    vnome = request.POST.get("nome")

    pessoa = Pessoa.objects.get(id = id)

    pessoa.nome = vnome

    pessoa.save()
    return redirect(teste)


def delete(request, id):

    pessoa = Pessoa.objects.get(id = id)

    pessoa.delete()
    return redirect(teste)


def adicionar_candidatos(request):

    return render(request, 'home/adicionar_candidatos.html')


def adicionar_vagas(request):


    return render(request, 'home/adicionar_vagas.html')




def salvar_candidato(request):

    candidato = Candidato()

    candidato.nome = request.POST.get("nome")


    candidato.endereco = request.POST.get("endereco")
    


    candidato.proficao = request.POST.get("proficao")

    candidato.contato = request.POST.get("contato")
    

    candidato.save()

    
    


    candidatos = { 

        'candidatos': Candidato.objects.all()


    }


    

    return render(request, 'home/candidatos.html', candidatos )



def ver_detalhes(request, id):
    

    candidato = Candidato.objects.get(id = id)

    
    

    return render(request, 'home/detalhes.html', {"candidato": candidato} )

    
def ver_detalhes_vaga(request, id):
    

    vaga = Vaga.objects.get(id = id)

    
    

    return render(request, 'home/detalhes_vagas.html', {"vaga": vaga} )

    




def editar_candidato(request, id):

    candidato = Candidato.objects.get(id = id) 

    return render(request, 'home/update_candidato.html', {"candidato": candidato})


def editar_vaga(request, id):

    vaga = Vaga.objects.get(id = id) 

    return render(request, 'home/update_vaga.html', {"vaga": vaga})




def update_candidato(request, id):

    hnome = request.POST.get("nome")

    hendereco = request.POST.get("endereco")

    hproficao = request.POST.get("proficao")

    candidato = Candidato.objects.get(id = id)
    candidato.nome = hnome
    candidato.endereco = hendereco

    candidato.proficao = hproficao

    candidato.save()

    candidatos = { 

        'candidatos': Candidato.objects.all()


    }


    

    return render(request, 'home/candidatos.html', candidatos )


def update_vaga(request, id):

    hnome = request.POST.get("nome")

    hendereco = request.POST.get("endereco")

    hproficao = request.POST.get("proficao")

    hcontato = request.POST.get("contato")

    vaga = Vaga.objects.get(id = id)
    vaga.nome = hnome
    vaga.endereco = hendereco

    vaga.proficao = hproficao

    vaga.contato = hcontato

    vaga.save()

    vagas = { 

        'vagas': Vaga.objects.all()


    }


    

    return render(request, 'home/vagas.html', vagas )


def delete_candidato(request, id):

    candidato = Candidato.objects.get(id = id)
    candidato.delete()

    candidatos = { 

        'candidatos': Candidato.objects.all()


    }


    

    return render(request, 'home/candidatos.html', candidatos )

def delete_vaga(request, id):

    vaga = Vaga.objects.get(id = id)
    vaga.delete()

    vagas = { 

        'vagas': Vaga.objects.all()


    }


    

    return render(request, 'home/vagas.html', vagas )

    

#adidionar vaga


def salvar_vagas(request):

    vaga = Vaga()

    vaga.nome = request.POST.get("nome")


    vaga.endereco = request.POST.get("endereco")
    


    vaga.atuacao = request.POST.get("atuacao")


    vaga.contato = request.POST.get("contato")
    

    vaga.save()

    
    


    vagas = { 

        'vagas': Vaga.objects.all()


    }


    

    return render(request, 'home/vagas.html', vagas )





