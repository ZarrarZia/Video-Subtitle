# Video Subtitle

Automatically generate subtitles for any video and burn them straight into the picture, using [OpenAI Whisper](https://github.com/openai/whisper) for speech recognition and [FFmpeg](https://ffmpeg.org/) for video processing.

Give it one or more video files and it will:

1. Extract the audio track.
2. Transcribe it with Whisper (or translate it to English).
3. Write a standard `.srt` subtitle file.
4. Render a new `.mp4` with the subtitles overlaid on the video.

Everything runs locally. No API key or internet connection is needed once the Whisper model has been downloaded.

## Features

- **Automatic transcription** in ~100 languages, with automatic language detection.
- **Translation to English** with `--task translate`.
- **Hard-coded subtitles**: the output video has the captions burned in, so it plays the same on any player or platform.
- **SRT export**: keep the `.srt` file alongside the video, or generate only the `.srt`.
- **Batch processing**: pass several videos in one command.
- **Selectable model size**, from `tiny` (fast) to `large` (most accurate).
- **Windows-friendly**:
  - finds FFmpeg installed with `winget` even if it isn't on your `PATH`;
  - handles Windows paths (drive letters, backslashes) correctly in FFmpeg's subtitle filter;
  - cleans up temporary `.srt` files you didn't ask to keep.

## Requirements

- Python 3.8 or newer
- [FFmpeg](https://ffmpeg.org/) installed on your system
- Optional: an NVIDIA GPU with CUDA for much faster transcription (Whisper falls back to the CPU automatically)

## Installation

### 1. Install FFmpeg

```bash
# Windows (winget)
winget install Gyan.FFmpeg

# Windows (Chocolatey)
choco install ffmpeg

# macOS (Homebrew)
brew install ffmpeg

# Ubuntu / Debian
sudo apt update && sudo apt install ffmpeg
```

### 2. Install Video Subtitle

Install directly from GitHub:

```bash
pip install git+https://github.com/ZarrarZia/Video-Subtitle.git
```

Or clone the repository and install it locally:

```bash
git clone https://github.com/ZarrarZia/Video-Subtitle.git
cd Video-Subtitle
pip install -e .
```

Either way, you get an `auto_subtitle` command.

## Usage

### Burn subtitles into a video

```bash
auto_subtitle path/to/video.mp4 -o output/
```

This creates `output/video.mp4` with the subtitles overlaid.

### Keep the `.srt` file as well

```bash
auto_subtitle path/to/video.mp4 -o output/ --output_srt True
```

### Generate only the `.srt` file (no video rendering)

```bash
auto_subtitle path/to/video.mp4 -o output/ --srt_only True
```

### Use a bigger model for better accuracy

```bash
auto_subtitle path/to/video.mp4 --model medium
```

### Set the spoken language instead of auto-detecting it

```bash
auto_subtitle path/to/video.mp4 --language ur
```

### Translate the speech into English subtitles

```bash
auto_subtitle path/to/video.mp4 --task translate
```

### Process several videos at once

```bash
auto_subtitle intro.mp4 lesson1.mp4 lesson2.mp4 -o output/
```

## Options

| Option | Default | Description |
| --- | --- | --- |
| `video` | *(required)* | One or more video files to process. |
| `--model` | `small` | Whisper model: `tiny`, `base`, `small`, `medium`, `large` (plus English-only `.en` variants such as `small.en`). |
| `--output_dir`, `-o` | `.` | Folder where output files are saved. Created if it doesn't exist. |
| `--output_srt` | `False` | Save the `.srt` file next to the subtitled video. |
| `--srt_only` | `False` | Only produce the `.srt` file; skip rendering the video. |
| `--task` | `transcribe` | `transcribe` keeps the original language; `translate` produces English subtitles. |
| `--language` | `auto` | Spoken language as an ISO code (`en`, `ur`, `hi`, `ar`, `es`, ...). `auto` detects it. |
| `--verbose` | `False` | Print transcription progress and debug messages. |

Run `auto_subtitle --help` for the full list, including every supported language code.

## Choosing a model

| Model | Approx. VRAM | Relative speed | Notes |
| --- | --- | --- | --- |
| `tiny` | ~1 GB | fastest | Good for quick drafts |
| `base` | ~1 GB | very fast | |
| `small` | ~2 GB | fast | Default; good for English |
| `medium` | ~5 GB | moderate | Recommended for non-English audio |
| `large` | ~10 GB | slowest | Best accuracy |

The model is downloaded the first time you use it and cached for later runs.

## Project structure

```
Video-Subtitle/
├── auto_subtitle/
│   ├── __init__.py
│   ├── cli.py          # Command-line entry point: audio extraction, transcription, rendering
│   └── utils.py        # SRT writing, timestamp formatting, helpers
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

## Troubleshooting

- **`ffmpeg` not found**: make sure FFmpeg is installed and on your `PATH`. Run `ffmpeg -version` to check. On Windows, open a new terminal after installing it.
- **Transcription is slow**: use a smaller model (`--model base`) or run on a machine with a CUDA-capable GPU.
- **Wrong language detected**: set it explicitly with `--language <code>`.

## Credits

This project is based on [auto-subtitle](https://github.com/m1guelpf/auto-subtitle) by Miguel Piedrafita and its contributors, extended with Windows compatibility fixes and SRT handling improvements.

## License

Released under the [MIT License](LICENSE).
