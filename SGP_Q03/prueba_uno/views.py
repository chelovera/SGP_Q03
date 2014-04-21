# coding=utf-8
# coding=utf-8
""" También establecemos un vínculo entre las dos instancias de modelo que creamos.
    Después de crear una nueva instancia de modelo de usuario, hacemos referencia en la instancia UserProfile
    con la línea profile.user = Usuario."""

from django.shortcuts import *
from .forms import UserForm, UserProfileForm

def register(request):
    # Obtenemos el contexto de la solicitud
    context = RequestContext(request)

    # Con un valor booleano decimos si el registro se ha realizado correctamente.
    # Se establece a False inicialmente.
    # El código cambia el valor en True cuando el registro se realiza correctamente.
    registered = False

    # Si es un HTTP POST, estamos interesados ​​en el procesamiento de los datos del formulario.
    if request.method == 'POST':
        # Captamos la informacion en forma cruda.
        # hacemos uso de ambos UserForm y UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Si las dos son válidas
        if user_form.is_valid() and profile_form.is_valid():
            # Se guardan los datos del formulario a la base de datos.
            user = user_form.save()

            # Hash de la contraseña con el método set_password.
            # Despues de la funcion hash, podemos actualizar el objeto de usuario.
            user.set_password(user.password)
            user.save()

            """ En UserProfile: 
            Esto retrasa la accion guardar del modelo hasta que estemos listos para evitar problemas de integridad."""

            profile = profile_form.save(commit=False)
            profile.user = user

           
          #  if 'picture' in request.FILES:
           #     profile.picture = request.FILES['picture']

            
            profile.save()

            # El registro de plantilla se ha realizado correctamente.
            registered = True

        # Si ocurren errores se muestran user_form.errors, profile_form.errors
        else:
            print user_form.errors, profile_form.errors

    # No es un HTTP POST, por lo que prestamos nuestro formulario mediante dos instancias ModelForm.
    # Estos formularios estarán en blanco, listo para la entrada del usuario.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Se renderiza la plantilla en función del contexto.
    return render_to_response(
            'prueba_uno/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


