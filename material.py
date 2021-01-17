from tuple import color, normalize, dot, reflect
from pattern import stripe_at_object

def lighting(material, object, light, point, eyev, normalv, in_shawdow = False):
    if material.pattern is not None:
        c = stripe_at_object(material.pattern, object, point)
    else:
        c = material.color
    effective_color = c * light.intensity
    lightv = normalize(light.position - point)
    ambient = effective_color * material.ambient
    light_dot_normal = dot(lightv, normalv)
    black = color(0, 0, 0)
    if light_dot_normal < 0:
        diffuse = black
        specular = black
    else:
        diffuse = effective_color * material.diffuse * light_dot_normal
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = black
        else:
            factor = reflect_dot_eye ** material.shininess
            specular = light.intensity * material.specular * factor
    if in_shawdow:
        return ambient
    else:
        return ambient + diffuse + specular

class material:

    def __init__(self):
        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
        self.pattern = None

    def __eq__(self, other):
        if (self.color == other.color and
            self.ambient == other.ambient and
            self.diffuse == other.diffuse and
            self.specular == other.specular and
            self.shininess == other.shininess and
            self.pattern == other.pattern):
            return True
        else:
            return False