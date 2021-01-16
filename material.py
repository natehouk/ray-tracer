from tuple import color, normalize, dot, reflect

def lighting(material, light, point, eyev, normalv):
    effective_color = material.color * light.intensity
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
            try:
                factor = reflect_dot_eye ** material.shininess
            except OverflowError:
                factor = 1
            specular = light.intensity * material.specular * factor
    return ambient + diffuse + specular

class material:

    def __init__(self):
        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, other):
        if (self.color == other.color and
            self.ambient == other.ambient and
            self.diffuse == other.diffuse and
            self.specular == other.specular and
            self.shininess == other.shininess):
            return True
        else:
            return False