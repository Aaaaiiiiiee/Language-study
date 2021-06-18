class Calculator
    @@_history = []

    def Calculator.history()
        for item in @@_history
            p item
        end
    end

    def initialize(v1, v2)
        @v1 = v1
        @v2 = v2
    end

    def setV1(v)
        if v.is_a?(Integer)
            @v1 = v
        else
            p 'you tried changing v1 by not integer'
        end
    end

    def add()
        result = @v1 + @v2
        @@_history.push("add : #{@v1}+#{@v2}=#{result}")
        return result
    end

    def subtract()
        result = @v1 - @v2
        @@_history.push("subtract : #{@v1}-#{@v2}=#{result}")
        return result
    end

    def info()
        return "Cal => v1 : #{@v1}, v2 : #{@v2}"
    end
end

class MultipleCalculator < Calculator
    def multiply()
        result = @v1 * @v2
        @@_history.push("multiply : #{@v1}*#{@v2}=#{result}")
        return result
    end

    def info()
        return "MultipleCalculator => #{super()}"
    end
end

class DivideCalculator < MultipleCalculator
    def divide()
        result = @v1 / @v2
        @@_history.push("divide : #{@v1}/#{@v2}=#{result}")
        return result
    end

    def info()
        return "DivideCalculator => #{super()}"
    end
end

c0 = Calculator.new(30, 60)
p c0.info()

c1 = MultipleCalculator.new(10, 10)
p c1.info()

c2 = DivideCalculator.new(20, 10)
p c2.info()

Calculator.history()