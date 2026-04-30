---
tags:
  - ai
  - midjourney
  - image-generation
  - prompts
  - creative
---

# MidJourney Guide

MidJourney is an AI image generation tool accessed via Discord or the MidJourney web interface. You write text prompts and it generates images. Unlike text LLMs, MidJourney is highly controlled through a combination of descriptive keywords and explicit parameters appended to the end of your prompt.

---

## Core Parameters

Parameters are appended to the end of a prompt using `--` syntax. They give you direct control over output dimensions, quality, style, and variation.

### --seed [number]

Controls the randomness starting point. The same seed + same prompt = more consistent results across runs.

- Use seed to create a series of images that share the same underlying style or feel
- To find a seed: react to a generated image with the envelope emoji in Discord — MidJourney will DM you the job details including the seed

```
--seed 12345
```

To generate multiple images with the same seed:

```
--sameseed 1234 --count 3
```

---

### --ar (Aspect Ratio)

Sets the output dimensions. Defaults to 1:1 if not specified.

| Value | Use Case |
|---|---|
| `--ar 16:9` | Widescreen / landscape / desktop wallpaper |
| `--ar 1:1` | Square (default) |
| `--ar 9:16` | Portrait / mobile / social stories |
| `--ar 4:3` | Classic photo / presentation |
| `--ar 3:2` | Standard photography ratio |

---

### --v (Version)

Selects which MidJourney model to use. Newer versions are more photorealistic and better at following complex prompts.

- `--v 6` — latest model, most photorealistic, strongest prompt adherence
- `--v 5.2` — previous generation, slightly more painterly aesthetic

---

### --style

Adjusts the aesthetic interpretation applied on top of your prompt.

- `--style raw` — less opinionated output; the model interprets your prompt more literally with less added "MidJourney aesthetic"
- `--style cute` — pushes toward a kawaii / soft / rounded aesthetic

---

### --q (Quality)

Controls how much GPU compute is used to render the image. Higher quality = more detail and coherence, but slower and uses more compute credits.

| Value | Effect |
|---|---|
| `--q 2` | Higher quality, more rendering time |
| `--q 1` | Default |
| `--q .5` | Faster, lower quality — good for quick drafts |

---

### --no (Negative Prompting)

Tells MidJourney what to exclude from the image. Useful for removing common unwanted elements.

```
--no text, watermark, blurry, low quality, extra limbs
```

---

### --chaos [0-100]

Controls how varied the four initial grid images are from each other. Low chaos = similar options; high chaos = wildly different options.

- `--chaos 0` — all four images are very similar
- `--chaos 100` — four very different interpretations of the prompt
- Good for exploration when you're not sure what direction you want

---

## Prompt Structure

A well-structured MidJourney prompt follows this general order:

```
[subject], [environment/setting], [mood/lighting], [style/medium], [artist reference], [parameters]
```

### Example

```
a lone samurai standing on a mountain peak, golden hour light, epic cinematic, digital painting, artstation, --ar 16:9 --v 6 --seed 42
```

**Breaking it down:**
- **Subject:** a lone samurai standing on a mountain peak
- **Lighting/mood:** golden hour light, epic cinematic
- **Style/medium:** digital painting
- **Quality signal:** artstation (community of professional digital artists — signals high quality)
- **Parameters:** aspect ratio 16:9, latest model, fixed seed

---

## Style Keywords Quick Reference

These keywords can be mixed and matched to steer the aesthetic of your images.

### Lighting
- `cinematic lighting`
- `golden hour`
- `volumetric light`
- `rim lighting`
- `studio lighting`
- `dramatic shadows`
- `soft diffused light`

### Quality Modifiers
- `highly detailed`
- `8k`
- `masterpiece`
- `best quality`
- `sharp focus`
- `intricate details`

### Art Styles & Mediums
- `oil painting`
- `watercolor`
- `digital art`
- `concept art`
- `illustration`
- `pencil sketch`
- `ink drawing`

### Aesthetics
- `dark fantasy`
- `cyberpunk`
- `cottagecore`
- `vaporwave`
- `brutalist`
- `solarpunk`
- `art deco`

### Rendering Engines
- `octane render`
- `unreal engine`
- `photorealistic`
- `hyperrealistic`
- `ray tracing`

### Artist References
Using an artist's name steers the model toward their visual style and technique.

- `by Greg Rutkowski` — epic fantasy, dramatic painterly compositions
- `by Alphonse Mucha` — art nouveau, ornate decorative borders
- `in the style of Studio Ghibli` — soft, hand-drawn, pastoral
- `by Zdzislaw Beksinski` — surreal, dark, dreamlike architecture
- `by Simon Stalenhag` — retrofuturistic, melancholy, sci-fi landscapes

---

## MidJourney Workflow

A repeatable process for getting polished results:

1. **Start simple** — write a prompt that establishes the core subject clearly
2. **Add modifiers** — layer in style, mood, and lighting keywords
3. **Set a seed** — lock in the seed once you find a result you like, to create consistent variations
4. **Use --no** — remove unwanted elements that keep appearing
5. **Upscale** — use U1, U2, U3, or U4 buttons to upscale your preferred image from the grid
6. **Vary** — use V1-V4 to explore variations of a selected image while keeping the composition
