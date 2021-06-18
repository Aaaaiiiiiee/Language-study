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
end

class MultipleCalculator < Calculator
    def multiply()
        result = @v1 * @v2
        @@_history.push("multiply : #{@v1}*#{@v2}=#{result}")
        return result
    end
end

class DivideCalculator < MultipleCalculator
    def divide()
        result = @v1 / @v2
        @@_history.push("divide : #{@v1}/#{@v2}=#{result}")
        return result
    end
end

c1 = MultipleCalculator.new(10, 10)
p 'add', c1.add()
p 'subtract', c1.subtract()
p 'multiply', c1.multiply()

c2 = DivideCalculator.new(20, 10)
p 'add', c2.add()
p 'subtract', c2.subtract()
p 'multiply', c2.multiply()
p 'divide', c2.divide()

Calculator.history()