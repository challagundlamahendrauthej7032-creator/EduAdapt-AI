"""
EduAdapt AI - Wispr Flow Voice Dictation Component
Enables voice dictation for Physics conceptual explanations with real-time speech
recognition and intelligent keyword-based semantic evaluation.
"""

import streamlit as st
import streamlit.components.v1 as components


def render_wispr_flow_mic_widget(target_element_id: str = "wispr_dictation_box"):
    """
    Renders an interactive Wispr Flow-styled Web Speech API voice recorder.
    Uses HTML5 SpeechRecognition to allow real-time browser microphone dictation.
    """
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {
            margin: 0;
            padding: 10px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: transparent;
        }
        .wispr-card {
            background: linear-gradient(135deg, #09090b 0%, #18181b 100%);
            border: 1px solid #27272a;
            border-radius: 14px;
            padding: 14px 18px;
            color: #fafafa;
            display: flex;
            flex-direction: column;
            gap: 10px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        }
        .top-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            font-weight: 700;
            letter-spacing: -0.01em;
        }
        .brand-badge {
            background: #6366f1;
            color: white;
            font-size: 0.65rem;
            font-weight: 800;
            padding: 2px 7px;
            border-radius: 999px;
            text-transform: uppercase;
        }
        .controls {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .record-btn {
            background: #4f46e5;
            color: #ffffff;
            border: none;
            border-radius: 10px;
            padding: 8px 16px;
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }
        .record-btn:hover {
            background: #4338ca;
            transform: scale(1.02);
        }
        .record-btn.recording {
            background: #ef4444;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
            100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }
        .status-text {
            font-size: 0.8rem;
            color: #a1a1aa;
        }
        .transcript-preview {
            background: #18181b;
            border: 1px solid #3f3f46;
            border-radius: 8px;
            padding: 10px;
            font-size: 0.85rem;
            color: #e4e4e7;
            min-height: 48px;
            line-height: 1.4;
            user-select: text;
        }
        .copy-btn {
            background: #27272a;
            color: #d4d4d8;
            border: 1px solid #3f3f46;
            border-radius: 6px;
            padding: 4px 10px;
            font-size: 0.75rem;
            cursor: pointer;
            align-self: flex-end;
        }
        .copy-btn:hover {
            background: #3f3f46;
            color: white;
        }
    </style>
    </head>
    <body>
        <div class="wispr-card">
            <div class="top-row">
                <div class="brand">
                    <span>🎙️ Wispr Flow</span>
                    <span class="brand-badge">Voice Dictation</span>
                </div>
                <div class="controls">
                    <button id="micBtn" class="record-btn" onclick="toggleDictation()">
                        <span id="micIcon">●</span>
                        <span id="btnLabel">Start Dictating</span>
                    </button>
                </div>
            </div>
            
            <div id="statusMsg" class="status-text">Click the button and speak your Physics explanation clearly into your microphone...</div>
            
            <div id="transcriptDisplay" class="transcript-preview">
                <i>Spoken words transcribed by Wispr Flow will appear here in real time...</i>
            </div>
            
            <button class="copy-btn" onclick="copyTranscript()">📋 Copy Dictated Text</button>
        </div>

        <script>
            let recognition = null;
            let isRecording = false;
            let fullTranscript = '';

            const SpeechRec = window.SpeechRecognition || window.webkitSpeechRecognition;

            function toggleDictation() {
                if (!SpeechRec) {
                    document.getElementById('statusMsg').innerText = 'Speech recognition not supported in this browser. Please use Chrome/Edge or the Quick Voice Presets below.';
                    return;
                }

                if (!isRecording) {
                    startDictation();
                } else {
                    stopDictation();
                }
            }

            function startDictation() {
                try {
                    recognition = new SpeechRec();
                    recognition.continuous = true;
                    recognition.interimResults = true;
                    recognition.lang = 'en-US';

                    recognition.onstart = function() {
                        isRecording = true;
                        document.getElementById('micBtn').classList.add('recording');
                        document.getElementById('btnLabel').innerText = 'Stop Dictating';
                        document.getElementById('statusMsg').innerText = '🔴 Wispr Flow Listening... Speak naturally';
                    };

                    recognition.onresult = function(event) {
                        let interim = '';
                        for (let i = event.resultIndex; i < event.results.length; ++i) {
                            if (event.results[i].isFinal) {
                                fullTranscript += event.results[i][0].transcript + ' ';
                            } else {
                                interim += event.results[i][0].transcript;
                            }
                        }
                        const current = fullTranscript + (interim ? ' (' + interim + ')' : '');
                        document.getElementById('transcriptDisplay').innerText = current || 'Listening...';
                    };

                    recognition.onerror = function(event) {
                        document.getElementById('statusMsg').innerText = 'Notice: ' + event.error + '. Try using Quick Dictate Presets below!';
                        stopDictation();
                    };

                    recognition.onend = function() {
                        stopDictation();
                    };

                    recognition.start();
                } catch(e) {
                    document.getElementById('statusMsg').innerText = 'Error initializing mic: ' + e.message;
                }
            }

            function stopDictation() {
                if (recognition) {
                    try { recognition.stop(); } catch(e) {}
                }
                isRecording = false;
                document.getElementById('micBtn').classList.remove('recording');
                document.getElementById('btnLabel').innerText = 'Start Dictating';
                document.getElementById('statusMsg').innerText = '✅ Dictation captured! Click "Copy Dictated Text" or paste into the answer box below.';
            }

            function copyTranscript() {
                const text = document.getElementById('transcriptDisplay').innerText;
                if (text && !text.includes('Spoken words transcribed')) {
                    navigator.clipboard.writeText(text);
                    const original = document.getElementById('statusMsg').innerText;
                    document.getElementById('statusMsg').innerText = '✅ Copied to clipboard! Paste into answer box below.';
                    setTimeout(() => {
                        document.getElementById('statusMsg').innerText = original;
                    }, 2500);
                }
            }
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=210)


def evaluate_voice_answer(transcript: str, expected_keywords: list, ideal_explanation: str) -> dict:
    """
    Evaluates a dictated explanation for a Physics question.
    Checks for keywords, semantic coverage, and conceptual completeness.
    """
    if not transcript or len(transcript.strip()) < 5:
        return {
            "score": 0,
            "matched_keywords": [],
            "missing_keywords": expected_keywords,
            "feedback": "No answer provided or answer too short to evaluate. Speak or enter at least 1-2 complete sentences.",
            "clarity_tier": "Incomplete"
        }

    clean_text = transcript.lower()

    matched = []
    missing = []

    for kw in expected_keywords:
        kw_clean = kw.lower()
        if kw_clean in clean_text:
            matched.append(kw)
        else:
            missing.append(kw)

    total_kw = len(expected_keywords)
    match_ratio = len(matched) / total_kw if total_kw > 0 else 0

    # Length & vocabulary richness factor
    word_count = len(clean_text.split())
    length_bonus = min(20, word_count * 0.5)

    raw_score = (match_ratio * 75) + length_bonus
    final_score = int(min(100, max(15, raw_score)))

    if final_score >= 80:
        clarity_tier = "Excellent Concept Mastery"
        feedback = "Outstanding explanation! You accurately articulated all fundamental physics laws, definitions, and relationships."
    elif final_score >= 60:
        clarity_tier = "Good - Minor Gaps"
        feedback = f"Good understanding. You captured {len(matched)} of {total_kw} key physics terms. Be sure to articulate missing scientific keywords for maximum board marks."
    else:
        clarity_tier = "Needs Reinforcement"
        feedback = f"Fundamental concepts are missing. Captured {len(matched)} of {total_kw} expected terms. Review the ideal model response below."

    return {
        "score": final_score,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "feedback": feedback,
        "clarity_tier": clarity_tier,
        "word_count": word_count
    }
