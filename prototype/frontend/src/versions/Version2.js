import { KeywordInput } from '../js_components/KeywordInput'
import TextField from '../js_components/TextField'
import { OptionButtons } from '../js_components/OptionButtons'
import Baseline from './Baseline'

class Version2 extends Baseline {

    render() {
        this.props.set_length(this.state.full_sen.length)
        return(
            <>
            <div>
                <KeywordInput 
                    g_started={this.generation_started} 
                    g_finished={this.generation_finished} 
                    disabled={this.state.isGenerating}
                    generate={this.generate_options}
                />
            </div>
            <div>
                <TextField 
                    stop={this.stopClock}
                    on_submit={this.generate_options} 
                    sentence={this.state.full_sen} 
                    handle_typing={this.handle_typing}
                    set_len={()=>{}}
                    disabled={true}
                />
            </div>
            <div>
                <OptionButtons
                    sentence_options={this.state.sen_options}
                    on_choose={this.option_choosed}
                    generate_new={this.new_options}
                />
            </div>
            </>
        )
    }
}

export default Version2;