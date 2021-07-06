import TextField from '../js_components/TextField'
import { KeywordInput } from '../js_components/KeywordInput'
import { ControllButtons } from '../js_components/ControllButtons'
import Baseline from './Baseline'

class Version1 extends Baseline {

    render() {
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
                Generated Text: 
                <TextField 
                    stop={this.stopClock}
                    on_submit={this.new_generation} 
                    sentence={this.state.sentence} 
                    handle_typing={this.handle_typing}
                    disabled={this.state.isGenerating}
                />
            </div>
            <div>
                <ControllButtons 
                    startClock={this.startClock} 
                    stopClock={this.stopClock}
                    redoGeneration={this.redoGeneration}
                    slowerGeneration={this.slowerGeneration}
                    fasterGeneration={this.fasterGeneration}
                    disabled={this.state.isGenerating}
                />
            </div>
            </>
        );
    }
}

export default Version1;