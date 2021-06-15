import { KeywordInput } from '../js_components/KeywordInput'
import { TextField } from '../js_components/TextField'
import { OptionButtons } from '../js_components/OptionButtons'

export function Version2(props) {

    return(
        <>
        <h2> version 2.0 </h2>
        <div>
            <KeywordInput 
                g_started={props.generation_started} 
                g_finished={props.generation_finished} 
                disabled={props.isGenerating}
                generate={props.generate_options}
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
            <OptionButtons
                sentence_options={props.sentence_options}
                on_choose={props.option_choosed}
            />
        </div>
        </>
    )
}