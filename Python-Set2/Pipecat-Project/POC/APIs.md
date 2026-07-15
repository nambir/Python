# APIs Used in Pipecat Voice ChatGPT Project



## Local Service APIs

### 1. Faster-Whisper STT Service
- **Purpose**: Local Speech-to-Text using OpenAI Whisper
- **Base URL**: `http://localhost:8000`
- **Docker Image**: `fedirz/faster-whisper-server:latest-cpu`
- **Endpoints**:
  - `POST /v1/audio/transcriptions` - OpenAI-compatible STT endpoint
  - `GET /docs` - Swagger documentation
  - `GET /health` - Health check
- **Model Used**: `Systran/faster-distil-whisper-medium.en`
- **Port**: 8000

### 2. Local TTS Service (Espeak)
- **Purpose**: Local Text-to-Speech using espeak-ng
- **Base URL**: `http://localhost:8001`
- **Custom Implementation**: FastAPI service
- **Endpoints**:
  - `GET /tts?text={text}` - Generate speech audio
  - `GET /health` - Health check
- **Voice**: English female (en+f3)
- **Output Format**: WAV audio
- **Port**: 8001

### 3. GPT4All Local API
- **Purpose**: Local Large Language Model
- **Base URL**: `http://localhost:4891/v1`
- **Endpoints**:
  - `POST /chat/completions` - OpenAI-compatible chat endpoint
  - `GET /models` - List available models
- **Model Used**: "Llama 3 8B Instruct" or "Mini Orca (Small)"
- **Port**: 4891
- **Requires**: GPT4All Desktop application running

### 4. Voice Gateway Service
- **Purpose**: Orchestrates STT → LLM → TTS pipeline
- **Base URL**: `http://localhost:8080`
- **Custom Implementation**: FastAPI service
- **Endpoints**:
  - `GET /` - Web interface
  - `POST /ask-audio` - Process audio input
  - `GET /get-greeting` - Generate greeting audio
  - `GET /health` - Health check
  - `GET /status` - Check all services status
- **Port**: 8080

### 5. Pipecat Voice Bot Service
- **Purpose**: Real-time voice bot with WebSocket support
- **Base URL**: `http://localhost:7860`
- **Custom Implementation**: FastAPI + WebSocket
- **Endpoints**:
  - `GET /` - Web interface
  - `WebSocket /ws` - Real-time communication
  - `GET /health` - Health check
  - `GET /services/status` - Check connected services
- **Port**: 7860

## Pipecat Framework APIs

### 1. Pipecat Core Services
- **STT**: `DeepgramSTTService` - Deepgram integration
- **LLM**: `OpenAILLMService` - OpenAI integration  
- **TTS**: `CartesiaTTSService` - Cartesia integration
- **VAD**: `SileroVADAnalyzer` - Voice Activity Detection
- **Turn Analysis**: `LocalSmartTurnAnalyzerV3` - Conversation turn detection

### 2. Pipecat Transport
- **Daily Transport**: `DailyTransport` - WebRTC via Daily.co
- **WebRTC Transport**: Generic WebRTC transport
- **RTVI Processor**: Real-time voice interface

## Docker Services Configuration

### STT Service (Faster-Whisper)
```yaml
image: fedirz/faster-whisper-server:latest-cpu
ports: ["8000:8000"]
environment:
  - ASR_MODEL=Systran/faster-distil-whisper-medium.en
  - NUM_WORKERS=1
  - BATCH_SIZE=8
```

### TTS Service (Custom Espeak)
```yaml
build: ./app/tts
ports: ["8001:8001"]
```

### Gateway Service
```yaml
build: ./app/server
ports: ["8080:8080"]
environment:
  - STT_URL=http://stt:8000/v1/audio/transcriptions
  - TTS_URL=http://tts:8001/tts
  - LLM_URL=http://host.docker.internal:4891/v1/chat/completions
```

## API Authentication & Configuration

### Required API Keys
- `DEEPGRAM_API_KEY` - For Deepgram STT service
- `OPENAI_API_KEY` - For OpenAI LLM service
- `CARTESIA_API_KEY` - For Cartesia TTS service
- `DAILY_API_KEY` - For Daily.co WebRTC (optional)

### Local Service URLs
- `LOCAL_STT_URL=http://localhost:8000`
- `LOCAL_TTS_URL=http://localhost:8001`
- `LOCAL_LLM_URL=http://localhost:4891`

## Health Check Endpoints

All services provide health check endpoints for monitoring:

- Gateway: `GET http://localhost:8080/health`
- STT: `GET http://localhost:8000/docs`
- TTS: `GET http://localhost:8001/health`
- LLM: `GET http://localhost:4891/v1/models`
- Voice Bot: `GET http://localhost:7860/health`

## WebSocket APIs

### Voice Bot WebSocket (`ws://localhost:7860/ws`)
**Message Types**:
- `text_input` - Process text input
- `voice_input` - Process audio input

**Status Updates**:
- `stt` - Speech-to-text processing
- `llm` - Language model processing  
- `tts` - Text-to-speech processing
- `conversation` - New conversation messages
- `ready` - System ready for input
- `error` - Error occurred

## Audio Format Support

### Input Formats
- WebM (from browser MediaRecorder)
- WAV (16kHz mono preferred)
- OGG/Opus

### Output Formats
- WAV (16kHz mono)
- Base64 encoded audio for WebSocket

## Rate Limits & Timeouts

### API Timeouts
- STT Processing: 120 seconds
- LLM Processing: 120 seconds (25 seconds for Mini Orca)
- TTS Processing: 30 seconds
- Health Checks: 3-5 seconds

### Service Limits
- Concurrent connections: Unlimited (limited by system resources)
- Audio file size: Limited by available memory
- Text length: Limited by LLM context window

## Error Handling

All services implement comprehensive error handling with:
- HTTP status codes
- JSON error responses
- Fallback mechanisms
- Service health monitoring
- Graceful degradation when services are unavailable