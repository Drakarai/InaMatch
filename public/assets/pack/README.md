# Paquete de sprites

Aquí van los gráficos que sustituyen a los provisionales (retratos, sprites de campo y escudos).
El juego lee `manifest.json` al arrancar; lo que no aparezca en él se dibuja por código.

```json
{
  "players": {
    "mark-evans": { "sprite": "sprites/mark-evans.png", "portrait": "portraits/mark-evans.png" },
    "axel-blaze": { "sprite": "sprites/axel-blaze.png", "portrait": "portraits/axel-blaze.png" }
  },
  "emblems": {
    "inazuma-national": "emblems/inazuma-national.png"
  }
}
```

- Las claves de `players` son los `id` de `src/data/teams/*.json`; las de `emblems`, el `id` del equipo.
- Las rutas son relativas a esta carpeta.
- **Sprite de campo**: el personaje de frente, con fondo transparente. Se escala a 46 px de alto.
- **Retrato**: cuadrado (96×96 o más grande). Se usa en la ficha, el panel de duelo y las supertécnicas.
- **Escudo**: cuadrado con fondo transparente.
