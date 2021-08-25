import TextField from '../js_components/TextField'
import { KeywordInput } from '../js_components/KeywordInput'
import { ControllButtons } from '../js_components/ControllButtons'
import Baseline from './Baseline'

class Version1 extends Baseline {

    render() {
        this.props.set_length(this.state.sentence.length)
        return(
            <>
            <div>
                <KeywordInput 
                    g_started={this.generation_started} 
                    g_finished={this.generation_finished} 
                    disabled={this.state.isGenerating}
                    generate={this.new_generation}
                />
            </div>
            <div>
                <TextField 
                    start={this.startClock} 
                    stop={this.stopClock}
                    on_submit={()=>{}} 
                    sentence={this.state.sentence} 
                    handle_typing={this.handle_typing}
                    set_len={()=>{}}
                    disabled={this.state.isGenerating}
                />
            </div>
            <div>
                <ControllButtons 
                    startClock={this.triggerStart} 
                    stopClock={this.stopClock}
                    redoGeneration={this.redoGeneration}
                    slowerGeneration={this.slowerGeneration}
                    fasterGeneration={this.fasterGeneration}
                    disabled={this.state.isGenerating}
                    running={this.state.running}
                />
            </div>
            </>
        );
    }
}

export default Version1;