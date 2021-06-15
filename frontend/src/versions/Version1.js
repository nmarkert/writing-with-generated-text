import { TextField } from '../js_components/TextField'
import { KeywordInput } from '../js_components/KeywordInput'
import { ControllButtons } from '../js_components/ControllButtons'

export function Version1(props) {
    return(
        <>
        <h2> version 1.1 </h2>
        <div>
        <KeywordInput 
            g_started={props.generation_started} 
            g_finished={props.generation_finished} 
            disabled={props.isGenerating}
            generate={props.new_generation}
        />
        </div>
        <div>
        Generated Text: 
        <TextField 
            stop={props.stopClock}
            on_submit={props.new_generation} 
            sentence={props.sentence} 
            handle_typing={props.handle_typing}
            disabled={props.isGenerating}
        />
        </div>
        <div>
        <ControllButtons 
            startClock={props.startClock} 
            stopClock={props.stopClock}
            redoGeneration={props.redoGeneration}
            slowerGeneration={props.slowerGeneration}
            fasterGeneration={props.fasterGeneration}
            disabled={props.isGenerating}
        />
        </div>
        </>
    )
}